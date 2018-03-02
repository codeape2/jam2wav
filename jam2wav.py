def jam2wav(jamfilecontents):
    riffindex = jamfilecontents.find(b'RIFF')
    return jamfilecontents[riffindex:]


def main():
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('jamfilename')
    parser.add_argument('wavfilename')
    args = parser.parse_args()

    with open(args.jamfilename, 'rb') as jamfile, open(args.wavfilename, 'wb') as wavfile:
        wavfile.write(jam2wav(jamfile.read()))


if __name__ == "__main__":
    main()