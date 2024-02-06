def repcalc1(match):
    return '%s%s%s%s%s' % (match.group(1), str(round(float(match.group(2))/12,2)), match.group(3), str(round(float(match.group(4))/12,2)), match.group(5))


editor.rereplace('(<BodyScaling>\r\n.*<X>)(.*)(</X>\r\n.*<Y>)(.*)(</Y>)', repcalc1)