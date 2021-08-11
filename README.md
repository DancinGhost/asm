# Getting started

So you are here because you like assembly/freestanding code, cool.

### Using gcc/clang to disassemble
`gcc -S tutorial.c -o tutorial.s -fverbose-asm`

`nano tutorial.s`
### Compiling assembly to executable
`gcc tutorial.s -o tutorial`

`./tutorial`
### Using odjump to disassemble
objdump -d --visualize-jumps -M intel -S tutorial.exe

### Compiling for no operating system or libraries
`gcc program.c -ffreestanding`

# Format

    .globl main

    main:
        # Write code here!

    .data

# Info
This repository supports x86_64/amd64, ARMv8-A and RISCV64 cpu architectures

Intel syntax is used here

.S files are ran through a preprocessor

.s files are fed straight into the assembler
