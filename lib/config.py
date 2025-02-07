from lib.core.parse_args import parse_args

args = parse_args()

config = {
    "logging": args.logging if args.logging else False,
    "model": args.model,
    "quiet": args.quiet if args.quiet else False,
    "temperature": args.temperature if args.temperature else 0.7,
    "streaming": args.streaming if args.streaming else True,
}
