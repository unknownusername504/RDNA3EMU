This is a simple non performant emulator of an AMD RDNA3 GPU designed to run HIP compiled asm.

The ISA can be found here : https://www.amd.com/content/dam/amd/en/documents/radeon-tech-docs/instruction-set-architectures/rdna3-shader-instruction-set-architecture-feb-2023_0.pdf

Current plans are:
1.) Implement all instructions in the ISA.
2.) Generate suitable asm using the HIP compiler. HIP is a source-portable language that can be compiled to run on either AMD or NVIDIA platform.
3.) Implement an interpreter to parse the compiled asm and execute instructions according to the file. This step should error if there are unmapped instructions or directives in the asm.
4.) Check for accuracy of results using some unit tests.
