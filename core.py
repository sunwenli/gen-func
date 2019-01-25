import make


def core_ios(rubbish_code_path, rubbish_code_num, cls_name, target):
    print 'make code %d... waiting' % rubbish_code_num
    make.make_code(rubbish_code_path, rubbish_code_num, cls_name, target)


def main():
    core_ios("/Users/sunwenli/Desktop/makecode10", 20, "SwlSDK", "DemoProj")


if __name__ == "__main__":
    main()