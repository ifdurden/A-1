import argparser

parser =argparse.ArgumnetParser(description="meow like a cat")
parser.add_argument("-n" , default=1 , type=int,help="The amount of times to meow")
args = parser.parse_args()

for _ in range(arg.n):
    print("meow")
