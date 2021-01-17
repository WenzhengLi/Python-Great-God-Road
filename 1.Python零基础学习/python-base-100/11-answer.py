import pretty_errors
pretty_errors.configure(
    separator_character='*',
    filename_display=pretty_errors.FILENAME_EXTENDED,
    line_number_first=True,
    display_link=True,
    lines_before=5,
    lines_after=2,
    line_color=pretty_errors.RED + '> ' + pretty_errors.default_config.line_color,
    code_color='  ' + pretty_errors.default_config.line_color,
    truncate_code=True,
    display_locals=True
)
pretty_errors.blacklist('c:/python')

'''
第一个月————1
第二个月————1
第三个月————2 = 1+1
第四个月————3 = 1+2
第五个月————5 = 2+3
第六个月————8 = 3+5
第七个月————13 = 5+8
第八个月————21 = 8+13
......      ......
由此
'''
f1 = f2 = 1
for i in range(1, 22):
    print('%12ld %12ld' % (f1, f2), end="")
    if (i % 3) == 0:
        print()
    f1 = f1 + f2
    f2 = f1+f2
