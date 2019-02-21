

from  selenium import  webdriver

driver = webdriver.Chrome()

driver.get('http://music.baidu.com/top/new')

eles = driver.find_elements_by_class_name('song-item')#找到歌曲列表每一行，列表保存

for ele in eles:#提取歌名 歌手 状态
   ele_song = ele.find_element_by_class_name("song-title")
   ele_singer = ele.find_element_by_class_name("singer")
   ele_statu = ele.find_element_by_class_name("status").find_element_by_tag_name('i')


   if ele_statu.get_attribute("class") == 'up':#根据状态过滤信息
       #过滤影视原声字段
       if '主题曲' in ele_song.text or '电影' in ele_song.text or '网剧' in ele_song.text:
           print('{0:{2}<20}:{1:<5}'.format(ele_song.text.split('（')[0],ele_singer.text,chr(12288)))
       else:
           print('{0:{2}<20}:{1:<5}'.format(ele_song.text, ele_singer.text, chr(12288)))


driver.quit()