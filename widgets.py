# Fix uncolored compass piece
def compass(wind_dir):
    g = '\033[1;32m'
    c = '\033[1;m'
    r = '\033[1;31m'
    if wind_dir == "North":
        print "             " + g + "<" + r + "." + c + g + ">" + c + c + "             "
        print "              " + g + "|" + c + "              "
        print "              " + g + "N" + c + "              "
        print "              " + g + "|" + c + "              "
        print "             )" + g + "|" + c + "(             "
        print "           )  " + g + "|" + c + "  (           "
        print "         )    " + g + "|" + c + "    (         "
        print "     W--------" + r + "|" + c + "--------E     "
        print "         )    |    (         "
        print "           )  |  (           "
        print "             )|(             "
        print "              |              "
        print "              S              "
    elif wind_dir == "South":
        print "              N              "
        print "              |              "
        print "             )|(             "
        print "           )  |  (           "
        print "         )    |    (         "
        print "     W--------" + r + "|" + c + "--------E     "
        print "         )    " + g + "|" + c + "    (         "
        print "           )  " + g + "|" + c + "  (           "
        print "             )" + g + "|" + c + "(             "
        print "              " + g + "|" + c + "              "
        print "              " + g + "S" + c + "              "
        print "              " + g + "|" + c + "              "
        print "             " + g + "<" + r + "." + c + g + ">" + c + c + "             "
    elif wind_dir == "East":
        print "              N              "
        print "              |              "
        print "             )|(             "
        print "           )  |  (           "
        print "         )    |    (         "
        print "     W--------" + r + "|" + c + "" + g + "--------E--<" + r + "." + c + g + ">" + c + c
        print "         )    |    (         "
        print "           )  |  (           "
        print "             )|(             "
        print "              |              "
        print "              S              "
    elif wind_dir == "West":
        print "              N              "
        print "              |              "
        print "             )|(             "
        print "           )  |  (           "
        print "         )    |    (         "
        print g + "<" + r + "." + c + g + ">--W--------" + c + r + "|" + c + "--------E     "
        print "         )    |    (         "
        print "           )  |  (           "
        print "             )|(             "
        print "              |              "
        print "              S              "
    elif wind_dir == "NE":
        print "                    " + g + "<" + r + "." + c + ">" + c + "      "
        print "              N     " + g + "/" + c + "        "
        print "              |    " + g + "/" + c + "         "
        print "             )|(  " + g + "/" + c + "          "
        print "           )  |  " + g + "/" + c + "           "
        print "         )    | " + g + "/" + c + "  (         "
        print "     W--------" + r + "|" + c + "--------E     "
        print "         )    |    (         "
        print "           )  |  (           "
        print "             )|(             "
        print "              |              "
        print "              S              "
    elif wind_dir == "NNE":
        print "                    " + g + "<" + r + "." + c + ">" + c + "      "
        print "              N     " + g + "/" + c + "        "
        print "              |    " + g + "/" + c + "         "
        print "             )|(  " + g + "/" + c + "          "
        print "           )  |  " + g + "/" + c + "           "
        print "         )    | " + g + "/" + c + "  (         "
        print "     W--------" + r + "|" + c + "--------E     "
        print "         )    |    (         "
        print "           )  |  (           "
        print "             )|(             "
        print "              |              "
        print "              S              "
    elif wind_dir == "ENE":
        print "                    " + g + "<" + r + "." + c + ">" + c + "      "
        print "              N     " + g + "/" + c + "        "
        print "              |    " + g + "/" + c + "         "
        print "             )|(  " + g + "/" + c + "          "
        print "           )  |  " + g + "/" + c + "           "
        print "         )    | " + g + "/" + c + "  (         "
        print "     W--------" + r + "|" + c + "--------E     "
        print "         )    |    (         "
        print "           )  |  (           "
        print "             )|(             "
        print "              |              "
        print "              S              "
    elif wind_dir == "SE":
        print "              N              "
        print "              |              "
        print "             )|(             "
        print "           )  |  (           "
        print "         )    |    (         "
        print "     W--------" + r + "|" + c + "--------E     "
        print "         )    | " + g + "\ " + c + "  (        "
        print "           )  |  " + g+ "\ " + c + "          "
        print "             )|(  " + g + "\ " + c + "         "
        print "              |    " + g + "\ " + c + "        "
        print "              S    " + g + "<" + r + "." + c + ">" + c + "       "
    elif wind_dir == "SSE":
        print "              N              "
        print "              |              "
        print "             )|(             "
        print "           )  |  (           "
        print "         )    |    (         "
        print "     W--------" + r + "|" + c + "--------E     "
        print "         )    | " + g + "\ " + c + "  (        "
        print "           )  |  " + g+ "\ " + c + "          "
        print "             )|(  " + g + "\ " + c + "         "
        print "              |    " + g + "\ " + c + "        "
        print "              S    " + g + "<" + r + "." + c + ">" + c + "       "
    elif wind_dir == "ESE":
        print "              N              "
        print "              |              "
        print "             )|(             "
        print "           )  |  (           "
        print "         )    |    (         "
        print "     W--------" + r + "|" + c + "--------E     "
        print "         )    | " + g + "\ " + c + "  (        "
        print "           )  |  " + g+ "\ " + c + "          "
        print "             )|(  " + g + "\ " + c + "         "
        print "              |    " + g + "\ " + c + "        "
        print "              S    " + g + "<" + r + "." + c + ">" + c + "       "
    elif wind_dir == "NW":
        print "       " + g + "<" + r + "." + c + ">" + c + "    N              "
        print "         " + g + "\ " + c + "   |              "
        print "          " + g + "\ " + c + " )|(             "
        print "           " + g + "\ " + c + " |  (           "
        print "         )  " + g + "\ " + c + "|    (         "
        print "     W--------" + r + "|" + c + "--------E     "
        print "         )    |    (         "
        print "           )  |  (           "
        print "             )|(             "
        print "              |              "
        print "              S              "
    elif wind_dir == "NNW":
        print "       " + g + "<" + r + "." + c + ">" + c + "    N              "
        print "         " + g + "\ " + c + "   |              "
        print "          " + g + "\ " + c + " )|(             "
        print "           " + g + "\ " + c + " |  (           "
        print "         )  " + g + "\ " + c + "|    (         "
        print "     W--------" + r + "|" + c + "--------E     "
        print "         )    |    (         "
        print "           )  |  (           "
        print "             )|(             "
        print "              |              "
        print "              S              "
    elif wind_dir == "WNW":
        print "       " + g + "<" + r + "." + c + ">" + c + "    N              "
        print "         " + g + "\ " + c + "   |              "
        print "          " + g + "\ " + c + " )|(             "
        print "           " + g + "\ " + c + " |  (           "
        print "         )  " + g + "\ " + c + "|    (         "
        print "     W--------" + r + "|" + c + "--------E     "
        print "         )    |    (         "
        print "           )  |  (           "
        print "             )|(             "
        print "              |              "
        print "              S              "
    elif wind_dir == "SW":
        print "              N              "
        print "              |              "
        print "             )|(             "
        print "           )  |  (           "
        print "         )    |    (         "
        print "     W--------" + r + "|" + c + "--------E     "
        print "         )  " + g + "/" + c + " |    (         "
        print "           " + g + "/" + c + "  |  (           "
        print "          " + g + "/" + c + "  )|(             "
        print "         " + g + "/" + c + "    |              "
        print "       " + g + "<" + r + "." + c + ">" + c + "    S              "
    elif wind_dir == "SSW":
        print "              N              "
        print "              |              "
        print "             )|(             "
        print "           )  |  (           "
        print "         )    |    (         "
        print "     W--------" + r + "|" + c + "--------E     "
        print "         )  " + g + "/" + c + " |    (         "
        print "           " + g + "/" + c + "  |  (           "
        print "          " + g + "/" + c + "  )|(             "
        print "         " + g + "/" + c + "    |              "
        print "       " + g + "<" + r + "." + c + ">" + c + "    S              "
    elif wind_dir == "WSW":
        print "              N              "
        print "              |              "
        print "             )|(             "
        print "           )  |  (           "
        print "         )    |    (         "
        print "     W--------" + r + "|" + c + "--------E     "
        print "         )  " + g + "/" + c + " |    (         "
        print "           " + g + "/" + c + "  |  (           "
        print "          " + g + "/" + c + "  )|(             "
        print "         " + g + "/" + c + "    |              "
        print "       " + g + "<" + r + "." + c + ">" + c + "    S              "
def rainfall(precip_today_in):
    cyan = '\033[1;36m'
    cend = '\033[1;m'
    if float(precip_today_in) > 0.00 and float(precip_today_in) < 1.00:
        print "         >6|-----|"
        print "          6|     |"
        print "          5|     |"
        print "          4|     |"
        print "          3|     |"
        print "          2|     |"
        print "          1|     |"
        print cyan + "         <1|||||||" + cend
    elif float(precip_today_in) > 0.99 and float(precip_today_in) < 2.00:
        print "         >6|-----|"
        print "          6|     |"
        print "          5|     |"
        print "          4|     |"
        print "          3|     |"
        print "          2|     |"
        print cyan + "          1|||||||" + cend
        print cyan + "         <1|||||||" + cend
    elif float(precip_today_in) > 1.99 and float(precip_today_in) < 3.00:
        print "         >6|-----|"
        print "          6|     |"
        print "          5|     |"
        print "          4|     |"
        print "          3|     |"
        print cyan + "          2|||||||" + cend
        print cyan + "          1|||||||" + cend
        print cyan + "         <1|||||||" + cend
    elif float(precip_today_in) > 2.99 and float(precip_today_in) < 4.00:
        print "         >6|-----|"
        print "          6|     |"
        print "          5|     |"
        print "          4|     |"
        print cyan + "          3|||||||" + cend
        print cyan + "          2|||||||" + cend
        print cyan + "          1|||||||" + cend
        print cyan + "         <1|||||||" + cend
    elif float(precip_today_in) > 3.99 and float(precip_today_in) < 5.00:
        print "         >6|-----|"
        print "          6|     |"
        print "          5|     |"
        print cyan + "          4|||||||" + cend
        print cyan + "          3|||||||" + cend
        print cyan + "          2|||||||" + cend
        print cyan + "          1|||||||" + cend
        print cyan + "         <1|||||||" + cend
    elif float(precip_today_in) > 4.99 and float(precip_today_in) < 6.00:
        print "         >6|-----|"
        print "          6|     |"
        print cyan + "          5|||||||" + cend
        print cyan + "          4|||||||" + cend
        print cyan + "          3|||||||" + cend
        print cyan + "          2|||||||" + cend
        print cyan + "          1|||||||" + cend
        print cyan + "         <1|||||||" + cend
    elif float(precip_today_in) > 5.99 and float(precip_today_in) < 7.00:
        print "         >6|-----|"
        print cyan + "          6|||||||" + cend
        print cyan + "          5|||||||" + cend
        print cyan + "          4|||||||" + cend
        print cyan + "          3|||||||" + cend
        print cyan + "          2|||||||" + cend
        print cyan + "          1|||||||" + cend
        print cyan + "         <1|||||||" + cend
    elif float(precip_today_in) > 6.99:
        print cyan + "         >6|||||||" + cend
        print cyan + "          6|||||||" + cend
        print cyan + "          5|||||||" + cend
        print cyan + "          4|||||||" + cend
        print cyan + "          3|||||||" + cend
        print cyan + "          2|||||||" + cend
        print cyan + "          1|||||||" + cend
        print cyan + "         <1|||||||" + cend
    else:
        print "         >6|-----|"
        print "          6|     |"
        print "          5|     |"
        print "          4|     |"
        print "          3|     |"
        print "          2|     |"
        print "          1|     |"
        print "         <1|-----|"
