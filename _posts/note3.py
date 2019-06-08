# -*- coding: utf-8 -*-
"""
blog note
"""
from time import gmtime
from time import strftime

def main():
    # init
    post_name = input("Please enter file name__> ")
    # title_name = input("Please input title_name__> ")
    time_tuple = strftime("%Y-%m-%d", gmtime())
    file_name = time_tuple + "-" + post_name + ".md"
    # title = "title: " + title_name + "\n"
    title = "title: " + "\n"
    content_set = "Content" + "\n" + "* any list" + "\n" + "{:toc}" + "\n\n"

    f = open(file_name, 'w')
    f.write('---\n')
    f.write("layout: post\n")

    f.write(title)
    f.write("categories:\n")
    f.write("- \n")
    #f.write("- DeepValue\n")
    f.write("---\n")
    # f.write("\n")
    f.write(content_set)
    f.write("## ChangeLog\n")
    f.write("\n")
    f.write("```\n")
    f.write("@Jeremy Anifacc\n")
    f.write(time_tuple)
    f.write("\n")
    f.write("```")

    f.close()

    print("Have a good journey!")

if __name__ == '__main__':
    main()
