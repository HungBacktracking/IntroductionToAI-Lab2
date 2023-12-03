import os
# from resolution import logic_resolution

INPUT_DIR = 'input/'
OUTPUT_DIR = 'output/'

def main():
    # Walkthrough files inside input directory.
    file_list = []
    for (dirpath, dirnames, filenames) in os.walk(INPUT_DIR):
        file_list.extend(filenames)
        break

    # Create output directory.
    if not os.path.exists(OUTPUT_DIR): os.makedirs(OUTPUT_DIR)

    for file in file_list:
        input = INPUT_DIR + file
        output = OUTPUT_DIR + file.replace('input', 'output')

        with open(input, 'r') as f:
            try:
                alpha = f.readline().strip()
                n = int(f.readline().strip())

                KB = []
                for _ in range(n):
                    clause = f.readline().strip()
                    KB.append(clause)
            except:
                print('There is an error when reading ', input)
                continue
            print(alpha)
            print(KB)
        # resolver = logic_resolution(KB, alpha)
        # resolver.pl_resolution()

        # with open(output, 'w') as f:
        #     resolver.print_output(f)
        # print('Solved', input, ', wrote to', output)

if __name__ == '__main__':
    main()