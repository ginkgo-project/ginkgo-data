#!/usr/bin/env python

fmt_string_first = """
    {{
        "name": "{}",
        "file": "{}"
    }}
""".strip("\n")
fmt_string_other = """,
    {{
        "name": "{}",
        "file": "{}"
    }}
""".strip("\n")
first = True

def fmt_string():
    global first
    if first:
        first = False
        return fmt_string_first
    return fmt_string_other


def print_jacobi_files(versions, kernels, precisions):
    for version in versions:
        for kernel in kernels:
            for precision, disp in precisions:
                print(fmt_string().format(
                        f"[{disp}] Block-Jacobi {kernel.capitalize()}, " +
                        f"v:{version}",
                        f"preconditioner/block_jacobi/" +
                        f"{version}/{precision}_{kernel}.json"),
                        end="")

def print_adaptive_jacobi_files(versions, kernels, precisions, storages):
    for version in versions:
        for kernel in kernels:
            for precision, disp in precisions:
                for storage, sdisp in storages[precision]:
                    print(fmt_string().format(
                            f"[{disp}] Adaptive Block-Jacobi {kernel.capitalize()} " +
                            f"({sdisp} blocks), v:{version}",
                            f"preconditioner/adaptive_block_jacobi/" +
                            f"{version}/{precision}_{storage}_{kernel}.json"),
                            end="")

def print_adaptive_jacobi_files_v2(versions, kernels, precisions, storages):
    for version in versions:
        for kernel in kernels:
            for precision, disp in precisions:
                for storage, sdisp in storages[precision]:
                    print(fmt_string().format(
                            f"[{disp}] Adaptive Block-Jacobi {kernel.capitalize()} " +
                            f"({sdisp} blocks), v:tp-{version}",
                            f"preconditioner/adaptive_block_jacobi/truncated_support/" +
                            f"{version}/{precision}_{storage}_{kernel}.json"),
                            end="")

def main():
    print("[")
    print_jacobi_files(
        ["row_major", "col_major"],
        ["generate", "apply"],
        [("double", "DP"), ("float", "SP")])
    print_adaptive_jacobi_files(
        ["row_major", "col_major", "no_padd", "interleaved",
         "interleaved_no_padd"],
        ["generate", "apply"],
        [("double", "DP"), ("float", "SP")],
        {
            "double" : [("double", "DP"), ("single", "SP"), ("half", "HP")],
            "float" : [("double", "SP"), ("single", "HP")]
        })
    print_adaptive_jacobi_files_v2(
        ["row_major", "col_major", "no_padd", "interleaved",
         "interleaved_no_padd"],
        ["generate", "apply"],
        [("double", "DP"), ("float", "SP")],
        {
            "double" : [
                ("full", "DP"), ("reduced", "SP"), ("reduced_twice", "HP"),
                ("truncated", "TP"), ("truncated_twice", "TTP"),
                ("truncated_reduced", "TSP")],
            "float" : [
                ("full", "SP"), ("reduced", "HP"), ("truncated", "TSP")]
        })
    print("\n]")

if __name__ == "__main__":
    main()
