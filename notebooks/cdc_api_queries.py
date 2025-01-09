# query1 groups by countyfips ONLY
# query2 groups by countyfips AND year


pm25_query1 = 'https://data.cdc.gov/resource/96sd-hxdt.json?$query=SELECT%0A%20%20%60countyfips%60%2C%0A%20%20avg(%60ds_pm_pred%60)%20AS%20%60avg_ds_pm_pred%60%2C%0A%20%20avg(%60ds_pm_stdd%60)%20AS%20%60avg_ds_pm_stdd%60%0AWHERE%20caseless_one_of(%60statefips%60%2C%20%226%22)%0AGROUP%20BY%20%60countyfips%60'



pm25_query2 = 'https://data.cdc.gov/resource/96sd-hxdt.json?$query=SELECT%0A%20%20%60countyfips%60%2C%0A%20%20%60year%60%2C%0A%20%20avg(%60ds_pm_pred%60)%20AS%20%60avg_ds_pm_pred%60%2C%0A%20%20avg(%60ds_pm_stdd%60)%20AS%20%60avg_ds_pm_stdd%60%0AWHERE%20caseless_one_of(%60statefips%60%2C%20%226%22)%0AGROUP%20BY%20%60countyfips%60%2C%20%60year%60'


oz_query1 = 'https://data.cdc.gov/resource/hf2a-3ebq.json?$query=SELECT%0A%20%20%60countyfips%60%2C%0A%20%20avg(%60ds_o3_pred%60)%20AS%20%60avg_ds_o3_pred%60%2C%0A%20%20avg(%60ds_o3_stdd%60)%20AS%20%60avg_ds_o3_stdd%60%0AWHERE%20%60statefips%60%20IN%20(%226%22)%0AGROUP%20BY%20%60countyfips%60'


oz_query2 = 'https://data.cdc.gov/resource/hf2a-3ebq.json?$query=SELECT%0A%20%20%60countyfips%60%2C%0A%20%20avg(%60ds_o3_pred%60)%20AS%20%60avg_ds_o3_pred%60%2C%0A%20%20avg(%60ds_o3_stdd%60)%20AS%20%60avg_ds_o3_stdd%60%2C%0A%20%20%60year%60%0AWHERE%20%60statefips%60%20IN%20(%226%22)%0AGROUP%20BY%20%60countyfips%60%2C%20%60year%60'