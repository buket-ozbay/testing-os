import dev.cat

def details(command):
    docpath = "/docs/commands/" + command + ".cdoc"
    dev.cat.read(docpath)