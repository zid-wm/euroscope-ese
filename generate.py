import glob

from pathlib import Path


def write_positions(out_file):
    out_file.write('[POSITIONS]\n')
    in_file_name = glob.glob('POF/*.pof')[-1]  # -1 gets us the latest POF file, if multiple are present

    with open(in_file_name, 'r') as in_file:
        positions = in_file.readlines()
        out_file.writelines(positions)

    out_file.write('\n')


def write_sidsstars(out_file):
    out_file.write('[SIDSSTARS]\n')
    in_files = glob.glob('SIDSSTARS/*/*.txt')

    for file_name in in_files:
        with open(file_name, 'r') as in_file:
            lines = in_file.readlines()
            out_file.writelines(lines)

    out_file.write('\n')


def write_ground(out_file):
    raise NotImplementedError


def main():
    airac = input('Enter current AIRAC: ')
    file_name = f'ESE/ZID {airac}.ese'

    # Create the ESE folder if it doesn't already exist
    Path('ESE/').mkdir(parents=True, exist_ok=True)

    with open(file_name, 'w+') as out_file:
        write_positions(out_file)
        write_sidsstars(out_file)


if __name__=='__main__':
    main()
