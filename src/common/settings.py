# This file contains the different links to gather our reviews from
# Amazon.fr website


import pickle as pk


# Settings
reviews_div_cls = 'review'

prod_urls = {'informatique':
[
        {
            'prod_id': 1,
            'prod_url':
                'https://www.amazon.fr/dp/B00VWEK4IG/ref=redir_mobile_desktop?_encoding=UTF8&aaxitk=.H.saUSQi0IDvqb-Ff4aow&hsa_cr_id=3200936120002&pd_rd_plhdr=t&pd_rd_r=01bb0b8a-0cca-4f13-b9af-530d3f06523e&pd_rd_w=6TgrH&pd_rd_wg=VzOfs&ref_=sbx_be_s_sparkle_td_asin_0_img',
            'rev_url':
                'https://www.amazon.fr/Avantree-Bluetooth-Adaptateur-équipements-Enceintes/product-reviews/B00VWEK4IG/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews',
            'rev_pages': 100,
            'rev_count': 1000

        },
        {
            'prod_id': 2,
            'prod_url':
                'https://www.amazon.fr/HP-302-Pack-cartouches-Authentiques/dp/B01LXLFF6H?ref_=Oct_s9_apbd_omwf_hd_bw_bN4CkB&pf_rd_r=V2TTM35Y3ZRBSP9XFVDS&pf_rd_p=3d37f0c5-041f-5707-bec0-94d62f6af77d&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=340858031&th=1',
            'rev_url':
                'https://www.amazon.fr/HP-302-Pack-cartouches-Authentiques/product-reviews/B01LXLFF6H/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews',
            'rev_pages': 100,
            'rev_count': 1000

        },
        {
            'prod_id': 3,
            'prod_url':
                'https://www.amazon.fr/Logitech-capteur-programmables-ordinateur-portable/dp/B07GS6ZB7T/ref=sr_1_6?brr=1&dchild=1&qid=1618071105&rd=1&s=computers&sr=1-6&th=1',
            'rev_url':
                'https://www.amazon.fr/Logitech-capteur-programmables-ordinateur-portable/product-reviews/B07GS6ZB7T/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews',
            'rev_pages': 100,
            'rev_count': 1000

        },
        {
            'prod_id': 4,
            'prod_url':
                'https://www.amazon.fr/microSDXC-SanDisk-Adaptateur-Performances-Applicatives/dp/B07FCMKK5X/ref=sr_1_4?brr=1&dchild=1&qid=1618071452&rd=1&s=computers&sr=1-4&th=1',
            'rev_url':
                'https://www.amazon.fr/microSDXC-SanDisk-Adaptateur-Performances-Applicatives/product-reviews/B07FCMKK5X/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews',
            'rev_pages': 100,
            'rev_count': 1000

        }
    ],
    'cuisine':
        [
            {
                'prod_id': 5,
                'prod_url':
                    'https://www.amazon.fr/AmazonBasics-Batterie-Cuisine-Anti-adh%C3%A9sive-pi%C3%A8ces/dp/B07481LPMF/ref=sr_1_5?_encoding=UTF8&c=ts&dchild=1&keywords=Casseroles%2C+po%C3%AAles+et+faitouts&qid=1618067686&s=kitchen&sr=1-5&ts_id=2969505031',
                'rev_url':
                    'https://www.amazon.fr/AmazonBasics-Batterie-Cuisine-Anti-adh%C3%A9sive-pi%C3%A8ces/product-reviews/B07481LPMF/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews',
                'rev_pages': 100,
                'rev_count': 1000

            },
            {
                'prod_id': 6,
                'prod_url':
                    'https://www.amazon.fr/céramique-Cadrim-Ensembles-couteaux-Couteaux/dp/B01N5JIZH5/ref=sr_1_4?_encoding=UTF8&c=ts&dchild=1&keywords=Couteaux+et+Ustensiles+de+Cuisine&qid=1618088450&s=kitchen&sr=1-4&ts_id=57698031',
                'rev_url':
                    'https://www.amazon.fr/céramique-Cadrim-Ensembles-couteaux-Couteaux/product-reviews/B01N5JIZH5/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews',
                'rev_pages': 100,
                'rev_count': 1000

            },
            {
                'prod_id': 7,
                'prod_url':
                    'https://www.amazon.fr/Homgeek-Milk-shake-Bouteilles-Portables-Couvercles/dp/B073XM1TTL?ref_=Oct_s9_apbd_otopr_hd_bw_b3rBLr&pf_rd_r=TC0P3DGNKKBWDWSEDFDM&pf_rd_p=16c350e6-3538-5eed-b91d-8bc2af2c901d&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=57004031',
                'rev_url':
                    'https://www.amazon.fr/Homgeek-Milk-shake-Bouteilles-Portables-Couvercles/product-reviews/B073XM1TTL/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews',
                'rev_pages': 100,
                'rev_count': 1000
            },
            {
                'prod_id': 8,
                'prod_url':
                    'https://www.amazon.fr/Moulinex-Intelligent-Multicuiseur-Recettes-Finition/dp/B00TQILY02?ref_=Oct_s9_apbd_omg_hd_bw_b3rBLr&pf_rd_r=TC0P3DGNKKBWDWSEDFDM&pf_rd_p=8c39304b-cce6-57e6-b16f-e4d3d7c89e6a&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=57004031',
                'rev_url':
                    'https://www.amazon.fr/Moulinex-Intelligent-Multicuiseur-Recettes-Finition/product-reviews/B00TQILY02/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews',
                'rev_pages': 100,
                'rev_count': 1000
            }
        ],
    'sports':
        [
            {
                'prod_id': 9,
                'prod_url':
                    'https://www.amazon.fr/Gritin-Résistance-Équipement-dExercices-Musculation/dp/B07L9WLKZQ?ref_=Oct_s9_apbd_otopr_hd_bw_bM2FLL&pf_rd_r=6FSMC9T9ZZE6ZNS4JFYA&pf_rd_p=9c37dc66-fb80-563a-854b-d52a81222d81&pf_rd_s=merchandised-search-11&pf_rd_t=BROWSE&pf_rd_i=325615031',
                'rev_url':
                    'https://www.amazon.fr/Gritin-Résistance-Équipement-dExercices-Musculation/product-reviews/B07L9WLKZQ/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews',
                'rev_pages': 100,
                'rev_count': 1000

            },
            {
                'prod_id': 10,
                'prod_url':
                    'https://www.amazon.fr/AMONAX-Roller-Roue-Exercice-Abdominaux-Musculation/dp/B081Z7BBMB?ref_=Oct_s9_apbd_oup_hd_bw_bM2FLL&pf_rd_r=6FSMC9T9ZZE6ZNS4JFYA&pf_rd_p=427a8d4e-455a-5ee8-bb93-7b8c5126c94b&pf_rd_s=merchandised-search-11&pf_rd_t=BROWSE&pf_rd_i=325615031',
                'rev_url':
                    'https://www.amazon.fr/AMONAX-Roller-Roue-Exercice-Abdominaux-Musculation/product-reviews/B081Z7BBMB/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews',
                'rev_pages': 100,
                'rev_count': 1000

            }

    ]

}

prod_cols = ['Prod_Title', 'Prod_Brnd', 'Prod_Rate', 'Prod_Eval', 'Prod_Price', 'Category', 'Nb_Revs', 'Prod_ID']
rev_cols = ['Rev_Title', 'Rev_Rate', 'Rev_Bdy', 'Rev_Hlp', 'Prod_ID']

# End Settings




if __name__ == '__main__':
    # To save settings into another file
    settings_file = open("settings.pkl", "wb")
    pk.dump(prod_urls, settings_file)
    settings_file.close()
