import lucs_tools
from time import sleep

class skyscanner(lucs_tools.internet.internet_base_util):

    BASE_LINK = 'https://www.skyscanner.com/transport/flights-from/FROM_AIRPORT/DEPART_DATE/RETURN_DATE/?adults=1&children=0&adultsv2=1&childrenv2=&infants=0&cabinclass=economy&rtn=1&preferdirects=false&outboundaltsenabled=ALTS_ENABLED&inboundaltsenabled=ALTS_ENABLED&ref=home&previousCultureSource=GEO_LOCATION&redirectedFrom=www.skyscanner.com&locale=en-GB&currency=USD&market=US&_mp=16a8d030756ea-03e7f4b2ae4014-e323069-190140-16a8d0307570_1557144041864&_ga=2.238286656.1539299884.1557143947-922572072.1557143947'

    @staticmethod
    def main(
        airport_code_1,
        airport_code_2,
        depart_date,
        return_date,
        alts_enabled=False,
        *args,
        **kwargs,        
    ):
        util = skyscanner()
        locations = (airport_code_1, airport_code_2)
        dates = [depart_date.split('/' if '/' in depart_date else '.'), return_date.split('/' if '/' in depart_date else '.')]
        dates = [''.join([date[-1]] + date[0:-1]) for date in dates]
        for location in locations:
            link = util.get_formatted_link(
                airport_code=location,
                dates=dates,
                alts_enabled=alts_enabled, 
            )
            util.open_link(link)
            return util

    def get_formatted_link(
        self,
        airport_code,
        dates,
        alts_enabled,
    ):
        link = self.BASE_LINK
        
        link = link.replace('ALTS_ENABLED', 'true' if alts_enabled else 'false')
        link = link.replace('FROM_AIRPORT', airport_code.lower())
        link = link.replace('DEPART_DATE', dates[0])
        link = link.replace('RETURN_DATE', dates[1])
        
        return link


        # elt = self.get_elements_with_param_matching_spec(
        #     'class_name',
        #     'BpkInput_bpk-input__XAfK8',
        # )[0]
        # elt.click()
        # elt = self.driver.switch_to_active_element()
        # elt.send_keys('{}\t\t'.format(searchkey))
        # elt = self.driver.switch_to_active_element()
        # elt.send_keys()

    def grab_data(
        self,
    ):
        browse_elts = True
        elts = self.get_elements_with_param_matching_spec('class_name', 'browse_data_route')
    # def inputdates(
    #     self,
    #     dar
    # )

class google(lucs_tools.internet.internet_base_util):

    @staticmethod
    def main(
        place1,
        place2,
        date1,
        date2,
    ):
        texts = []
        util = google()
        for place in [place1, place2]:
            # so verbose it comments itself ;?0
            util.openlink()
            util.inputsearch(place)
            util.inputdates(date1, date2)
            util.clicksearch()

            # grab data
            texts.append(util.scraperesults())
        
        return texts

    def openlink(
        self
    ):
        self.open_link('https://www.google.com/flights?hl=en')

    def inputsearch(
        self,
        searchkey
    ):
        elt = self.get_elements_with_param_matching_spec('class_name', 'flt-input')[0]
        elt.click()
        elt = self.driver.switch_to_active_element()
        sleep(0.4)
        elt = self.driver.switch_to_active_element()
        elt.send_keys('{}'.format(searchkey))
        sleep(1)
        elt = self.driver.switch_to_active_element()
        elt.send_keys('\n')
        sleep(1)

    def inputdates(
        self,
        date1,
        date2,
    ):
        #print(i, datekey)
        date = self.get_elements_with_param_matching_spec('class_name', 'gws-flights-form__date-content')[0]
        date.click()
        sleep(0.5)
        date = self.driver.switch_to_active_element()
        sleep(0.5)
        date.send_keys('{}\t{}'.format(date1, date2))
        sleep(0.5)

        elt = self.get_element_with_param_matching_spec('class_name', 'eE8hUfzg9Na__button')

        elt.click()

    def clicksearch(
        self,
    ):
        elt = self.get_elements_with_param_matching_spec('class_name', 'flt-form-sb')[0]
        sleep(1)
        elt.click()

    def scraperesults(
        self,
    ):
        elt = self.get_elements_with_param_matching_spec('class_name', 'VIUEWc')[0]
        return elt.text.split('\n')
