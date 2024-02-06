def repcalc1(match):
    return '%s%s%s%s' % (match.group(1), str(float(match.group(2))/5), match.group(3), str(float(match.group(4))/2))


editor.rereplace('(<BodyScaling>\r\n.*<X>)(\d*)(</X>\r\n.*<Y>)(\d*)', repcalc1)