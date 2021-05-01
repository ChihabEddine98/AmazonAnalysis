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
                'https://www.amazon.fr/Exclusif-Microsoft-Surface-Windows-tactile/dp/B08CNLLM57/ref=sr_1_11?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=Microsoft+Surface&qid=1618066809&s=computers&sr=1-11',
            'rev_url':
                'https://www.amazon.fr/Exclusif-Microsoft-Surface-Windows-tactile/product-reviews/B08CNLLM57/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews',
            'rev_pages': 5,
            'rev_count': 50

        },
        {
            'prod_id': 2,
            'prod_url':
                'https://www.amazon.fr/HP-302-Pack-cartouches-Authentiques/dp/B01LXLFF6H?ref_=Oct_s9_apbd_omwf_hd_bw_bN4CkB&pf_rd_r=V2TTM35Y3ZRBSP9XFVDS&pf_rd_p=3d37f0c5-041f-5707-bec0-94d62f6af77d&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=340858031&th=1',
            'rev_url':
                'https://www.amazon.fr/HP-302-Pack-cartouches-Authentiques/product-reviews/B01LXLFF6H/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews',
            'rev_pages': 10,
            'rev_count': 100

        }
    ],
    'cuisine':
        [
            {
                'prod_id': 3,
                'prod_url':
                    'https://www.amazon.fr/AmazonBasics-Batterie-Cuisine-Anti-adh%C3%A9sive-pi%C3%A8ces/dp/B07481LPMF/ref=sr_1_5?_encoding=UTF8&c=ts&dchild=1&keywords=Casseroles%2C+po%C3%AAles+et+faitouts&qid=1618067686&s=kitchen&sr=1-5&ts_id=2969505031',
                'rev_url':
                    'https://www.amazon.fr/AmazonBasics-Batterie-Cuisine-Anti-adh%C3%A9sive-pi%C3%A8ces/product-reviews/B07481LPMF/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews',
                'rev_pages': 5,
                'rev_count': 50

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
