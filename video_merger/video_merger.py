import sys
import ffmpeg


if __name__ == '__main__':
    print(sys.argv)
    print(len(sys.argv))
    print(str(sys.argv[len(sys.argv) - 1]))
    list = open("list.txt", "w")
    for i in range(1, len(sys.argv) - 1):
        list.write("file {}\n".format(sys.argv[i]))
    list.close()
    ffmpeg.input("list.txt", format='concat', safe=0).output(sys.argv[len(sys.argv) - 1], c='copy').run()
