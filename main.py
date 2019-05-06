import twoflights

# twoflights.google.main(
#     place1='Geneva',
#     place2='Amsterda',
#     date1='Fri, 17 May',
#     date2='Mon, 20 May',
# )

ret = twoflights.skyscanner.main(
    'GVA',
    'AMS',
    '05/17/19',
    '05/20/19',
)