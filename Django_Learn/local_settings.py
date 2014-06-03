'''
Created on 2013-5-16

@author: computer
'''

SOCIALOAUTH_SITES = {
    'renren': ('socialoauth.sites.renren.RenRen', 1, '»À»ÀÕ¯',
               {
                'redirect_uri': 'http://test.org/account/oauth/renren',
                'client_id': 'YOUR ID',
                'client_secret': 'YOUR SECRET',
                'scope': ['publish_feed', 'status_update']
               }
    ),
 
    'weibo': ('socialoauth.sites.weibo.Weibo', 2, '–¬¿ÀŒ¢≤©',
              {
                'redirect_uri': 'http://test.org/account/oauth/weibo',
                'client_id': 'YOUR ID',
                'client_secret': 'YOUR SECRET',
              }
    ),

    'qq': ('socialoauth.sites.qq.QQ', 3, 'QQ’ ∫≈',
              {
                'redirect_uri': 'http://test.org/account/oauth/qq',
                'client_id': '523720676',
                'client_secret': '099438ygs',
              }
    ),


}