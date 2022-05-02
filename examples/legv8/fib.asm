    ADDI X16, XZR, 20 // Number of fib iterations
    ADDI X15, XZR, 0  // Mem addr for storing
    ADDI X5, XZR, 0   // Initial values
    ADDI X6, XZR, 1
fib:
    ADD  X7, X6, X5   // Calc next fib number
    ADDI X5, X6, 0
    ADDI X6, X7, 0
    SUBI X16, X16, 1  // Dec fib iterator
    ADDI X0, X5, 0

    STUR X0, [X15, 0] // Store fib value
    ADDI X15, X15, 8

    CBNZ X16, =fib