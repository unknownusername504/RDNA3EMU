rodata = subprocess.check_output(
    [
        "/opt/rocm/llvm/bin/llvm-objdump",
        "-s",
        "-j",
        ".rodata",  # Display the .rodata section as raw bytes
        "--mcpu=gfx1100",
        "--arch=amdgcn",
        "-",
    ],
    input=obj_data,
)

# Decode the output from bytes to string
output = rodata.decode()

# Split the output into lines
lines = output.split("\n")

# Remove the first 3 lines as they are not needed
lines = lines[3:]

# Remove the decoded ASCII characters from each line
lines = [
    line.split("  ")[0]
    for line in lines
    if line and not line.startswith("<stdin>:	file format")
]

# Remove the leading and trailing spaces and tabs from each line
lines = [line.strip() for line in lines]

# Check if the last line needs padding
last_line = lines[-1]
last_line_addr = last_line[:5]
last_line = last_line[5:]
# Calculate the number of zeros to add
num_zeros = 32
# Add the zeros to the end of the last line
padding = "0" * num_zeros

# Add spaces every 8 zeros in the padding
padding = " ".join([padding[i : i + 8] for i in range(0, len(padding), 8)])

padding = (padding[len(last_line) :]).strip()

# Add the padding to the last line
lines[-1] = last_line_addr + last_line + padding

# Convert output in the form of :
# 05c0 00000000 00000000 18000000 00000000
# to:
# global_preload_b64 0x0000000000000000 offset:05c0
# global_preload_b64 0x1800000000000000 offset:05c8
new_lines = []
for idx, line in enumerate(lines):
    data = line[6:]
    data = data.replace(" ", "")
    data = data.replace("\t", "")
    data0 = data[:16]
    data1 = data[16:]
    offset = line[:6]
    # Convert the offset to a hex number
    offset = int(offset, 16)
    # Skip if the data is all zeros
    if data0 != "0" * 16:
        new_lines.append(
            "\t" + "global_preload_b64 0x" + data0 + " offset:" + hex(offset)
        )
    if data1 != "0" * 16:
        new_lines.append(
            "\t" + "global_preload_b64 0x" + data1 + " offset:" + hex(offset + 8)
        )

# Join the lines back together into a single string
rodata = ("\n".join(new_lines)).encode()

# Prepend the rodata to the code section of the objdump which begins at line 7
# but objdump is encoded so we need to insert after the 7th '\n'
obj_data = obj_data.split(b"\n")
obj_data = obj_data[:7] + [rodata] + obj_data[7:]
obj_data = b"\n".join(obj_data)
