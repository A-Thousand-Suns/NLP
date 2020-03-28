import argparse

def parst_args():
    parse = argparse.ArgumentParser(description='run wordSeg function')

    parse.add_argument('--input', required=True, help='input the file path')

    parse.add_argument('--dic', required=True, help='input the dictionary path')
