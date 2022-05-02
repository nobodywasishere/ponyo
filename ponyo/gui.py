#!/usr/bin/env python

import PySimpleGUIQt as sg
from copy import deepcopy as dpcp

font = ("mono", 10)
button_size = (10, 0.75)

layout = [
    [
        sg.Stretch(),
        sg.Button("Reset", size=button_size),
        sg.Button("Back", size=button_size),
        sg.Button("Stop", size=button_size),
        sg.Button("Step", size=button_size),
        sg.Button("Run", size=button_size),
        sg.Stretch(),
        sg.Text("Speed: 200 ", font=font, key="speedText"),
        sg.Slider(
            range=(0, 500),
            default_value=200,
            size=(1, 0.15),
            orientation="horizontal",
            font=font,
            key="timeoutSlider",
        ),
        sg.Stretch(),
    ],
    [
        sg.Stretch(),
        sg.Multiline(
            "",
            size=(50, 30),
            key="codePane",
            font=font,
            disabled=True,
            # write_only=True,
            # no_scrollbar=True,
            # expand_x=True,
            # expand_y=True,
        ),
        sg.Multiline(
            "",
            size=(40, 30),
            key="regPane",
            disabled=True,
            font=font,
            # no_scrollbar=True,
            # write_only=True,
            # expand_x=True,
            # expand_y=True,
        ),
        sg.Stretch(),
    ],
    [
        sg.Stretch(),
        sg.Multiline(
            "",
            size=(90, 2),
            key="flagPane",
            disabled=True,
            font=font,
            # no_scrollbar=True,
            # write_only=True,
            # expand_x=True,
            # expand_y=True,
        ),
        sg.Stretch(),
    ],
    [
        sg.Stretch(),
        sg.Multiline(
            "",
            size=(90, 16),
            key="memPane",
            disabled=True,
            font=font,
            # write_only=True,
            # no_scrollbar=True,
            # expand_x=True,
            # expand_y=True,
        ),
        sg.Stretch(),
    ],
]


def currCode(sim, low: int = -5, high: int = 5) -> str:
    """String showing surrounding code to PC

    Args:
        sim (ponyo.Simulator): Current Simulator instance
        low (int, optional): Number of lines before PC. Defaults to -5.
        high (int, optional): Number of lines after PC. Defaults to 5.

    Returns:
        str: Section of code arround PC
    """
    imem = sim.imem_raw
    pc = sim.mem.pc
    out = []
    for i in range(pc + low, pc + high):
        if i < 0 or i >= sim.imem_len:
            out.append("")
            continue

        if i == pc:
            prefix = "--> | "
        else:
            prefix = f"{i:3} | "

        out.append(f"{prefix}{imem[i]}")
    return "\n".join(out)


def gui(sim):
    """Runs an interactive GUI for the simulator using PySimpleGUIQt

    Args:
        sim (ponyo.Simulator): Starting Simulator with loaded imem/dmem
    """

    # Create the Window
    window = sg.Window("Ponyo - ISA Simulator", layout)
    # Event Loop to process "events"
    run = False
    end_code = False
    prev_sims = []
    timeout = 200
    while sim.mem.pc < sim.imem_len or end_code:

        event, values = window.read(timeout=timeout)

        if "timeoutSlider" in values:
            timeout = values["timeoutSlider"]
            window["speedText"].update(value=f"Speed: {timeout} ")

        if event == sg.WIN_CLOSED:
            break
        elif event == "__TIMEOUT__" and not run:
            continue
        elif event == "Reset":
            sim.mem.reset()
            prev_sims = []
            run = False
        elif event == "Back":
            if len(prev_sims) > 0:
                sim.mem = dpcp(prev_sims[-1])
                prev_sims = prev_sims[:-1]
        elif not end_code:
            prev_sims.append(dpcp(sim.mem))
            if len(prev_sims) > 100:
                prev_sims = prev_sims[1:]

        if run and not end_code:
            if "//$break" in sim.imem_raw[sim.mem.pc]:
                run = False

        window["codePane"].update(value=currCode(sim, -16, 16))
        window["memPane"].update(value=sim.mem.mem2str())
        window["regPane"].update(value=sim.mem.reg2str())
        window["flagPane"].update(value=sim.mem.pcfl2str())

        if event == "Stop":
            run = False
        elif event == "Step" and not end_code:
            run = False
            sim.step()
        elif (event == "Run" or run) and not end_code:
            run = True
            sim.step()

        if sim.mem.pc == sim.imem_len:
            end_code = True
            run = False
        else:
            end_code = False

    window.close()
