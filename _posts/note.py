# -*- coding: utf-8 -*-
"""
blog note
"""
from time import gmtime
from time import strftime

def main():
    # init
    post_name = raw_input("请输入博文英文名__> ")
    time_tuple = strftime("%Y-%m-%d", gmtime())
    file_name = time_tuple + "-" + post_name + ".md"

    f = open(file_name, 'w')
    f.write('---\n')
    f.write("layout: post\n")
    f.write("title: \n")
    f.write("categories:\n")
    f.write("- \n")
    f.write("---\n")

    f.close()

    print("Have a good journey!")

if __name__ == '__main__':
    main()
