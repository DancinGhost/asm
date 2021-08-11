# Getting started

Alright so you are here because you like assembly/freestanding code, cool.


`gcc -S tutorial.c -o tutorial.s`

`gcc tutorial.s -o tutorial`

`./tutorial`


`gcc program.c -ffreestanding`

.S files are ran through a preprocessor

.s files are fed straight into the assembler

# Format

    .globl main

    main:
        # Write code here!

    .data

# Info
This repository supports x86_64/amd64, ARMv8-A and RISCV64 cpu architectures.

# Mise en route

Bon, vous êtes ici parce que vous aimez l'assemblage et le code libre, c'est cool.


`gcc -S tutorial.c -o tutorial.s`

`gcc tutorial.s -o tutorial`

`.tutorial`


`gcc program.c -ffreestanding`

Les fichiers .s passent par un préprocesseur.

Les fichiers .S sont introduits directement dans l'assembleur

# Format

    .globl main

    main:
        # Écrire le code ici !

    .data

# Info
Ce référentiel prend en charge le x86_64/amd64, ARMv8-A and RISCV64 architectures de processeurs
