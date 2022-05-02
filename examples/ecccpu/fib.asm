main:
    LDI r0 1
    LDI r1 1
    LDI r2 fib
    LDI r3 0
    STR r0 r3
    ; STD r0 14
    INC r3
    STR r1 r3
    ; STD r1 14
    DEC r3
fib:
    LDR r0 r3
    INC r3
    LDR r1 r3
    ADD r1 r0
    LDI r2 end
    JMP r2 3
    ; break
    INC r3
    STR r1 r3
    ; STD r1 14
    DEC r3
    LDI r2 fib
    JMP r2
end:
