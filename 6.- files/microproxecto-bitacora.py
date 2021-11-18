
def version1():
    from datetime import datetime
    now = str(datetime.now())
    text = input("Entrada de bitácora %s: " % now)
    file = open("Bitácora %s.txt" % now,"w")
    file.write("%s\n\n%s" % (now,text))
    file.close()

def version2():
    from datetime import datetime

    now = str(datetime.now())
    lines = []
    line = None

    while line != "":
        line = input("Linea %s: " % str(len(lines)+1))
        if line != "": lines.append(line)

    file = open("Bitácora %s.txt" % now,"w")
    file_content = "\n".join(lines)
    file.write("%s\n\n%s\n" % (now,file_content))
    file.close()

def version3():
    from datetime import datetime

    now = str(datetime.now())
    lines = []
    line = None

    while line != "":
        line = input("Linea %s: " % str(len(lines)+1))
        if line != "": lines.append(line)

    file_name = "Bitácora %s.txt" % now
    file_content = "\n".join(lines)

    try:
        file = open(file_name,"w")
        file.write("%s\n\n%s\n" % (now,file_content))
    except Exception as err:
        print("Oooops! no hemos podido guardar tu texto:\n%s" % err)
        if not file.closed: file.close()
    finally:
        file.close()
        print("Guardada bitácora %s." % file_name)


    

version3()