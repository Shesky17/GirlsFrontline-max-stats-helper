from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


def compare(str_type, first, second):
    result = []
    site = "https://en.gfwiki.com/wiki/List_of_" + str_type.strip().upper() + "_by_Maximum_Stats"

    # gflwiki checks for user agent otherwise you'll get 403
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site, headers=hdr)
    page = urlopen(req)
    bs = BeautifulSoup(page, features="lxml")

    # iter next first entry
    tbody = bs.tbody
    tr_list = tbody.find_all("tr")
    iter_tr_list = iter(tr_list)
    next(iter_tr_list)

    for tr in iter_tr_list:
        td_list = tr.find_all("td")
        href_list = td_list[1].find("a")
        if first.lower() == href_list.attrs['title'].lower() or second == href_list.attrs['title'].lower():
            result.append([td_list[1].text.strip('\n'),
                           td_list[0].text.strip('\n'),
                           td_list[2].text.strip('\n'),
                           td_list[3].text.strip('\n'),
                           td_list[4].text.strip('\n'),
                           td_list[5].text.strip('\n'),
                           td_list[6].text.strip('\n')])
            print("T-doll name: " + td_list[1].text +
                  "Index: " + td_list[0].text +
                  "Max Dmg: " + td_list[2].text +
                  "Max EVA: " + td_list[3].text +
                  "Max ACC: " + td_list[4].text +
                  "Max ROF: " + td_list[5].text +
                  "Max HP: " + td_list[6].text +
                  "\n")
    # debug print
    # for doll in result:
    #     print(doll)
    #     print()


# prompt for input
t_doll_type = input("T-doll type (HG, SMG, AR, RF). Doesn't matter upper case or lower.\n")
first_pmt = input("First t-doll name.\n")
second_pmt = input("T-doll to compare. (Leave it empty if only want to look up the previous one)\n")
compare(t_doll_type, first_pmt, second_pmt)
