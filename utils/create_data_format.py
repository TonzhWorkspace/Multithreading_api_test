# coding=utf-8
# __author__ = 'Gz'
import json


# 根据数据类型生成校验参数
def data_type_case(data):
    if isinstance(data, str) and 'http' in data:
        data_type = 'HTTP'
    elif isinstance(data, bool):
        data_type = 'Bool'
    elif isinstance(data, str):
        data_type = 'Str'
    elif isinstance(data, int):
        data_type = 'Int'
    else:
        # 处理了None
        data_type = '$$$'
    return data_type


# content数据清洗
# 把接口中的值清理了
# 如果遇到的是一个LIST那么默认其中所有的内容都是一致的只保留一个模板内容
def ergodic_list(data):
    if isinstance(data, list):
        for i in range(len(data)):
            if i == 0:
                if isinstance(data[i], str) or isinstance(data[i], int) or isinstance(data[i], bool) or data[i] == None:
                    data[i] = data_type_case(data[i])
                    print('list中存放的不是dict')
                else:
                    ergodic_list(data[i])
            else:
                data[i] = None
    elif isinstance(data, dict):
        for key in data.keys():
            if isinstance(data[key], str) or isinstance(data[key], int) or isinstance(data[key], bool) or data[
                key] == None:
                data[key] = data_type_case(data[key])
            else:
                ergodic_list(data[key])
    return data


def ergodic_new(data):
    if isinstance(data, list):
        for i in range(len(data)):
            if isinstance(data[i], str) or isinstance(data[i], int) or isinstance(data[i], bool) or data[i] == None:
                data[i] = data_type_case(data[i])
            else:
                ergodic_new(data[i])
    elif isinstance(data, dict):
        for key in data.keys():
            if isinstance(data[key], str) or isinstance(data[key], int) or isinstance(data[key], bool) or data[
                key] == None:
                data[key] = data_type_case(data[key])
            else:
                ergodic_new(data[key])
    return data


# 异常数据处理
# 需要根据具体情况添加主要解决不识别问题
def data_clear(data):
    if isinstance(data, bytes):
        data = data.decode('utf-8')
    data = json.loads(data)
    data = ergodic_list(data)
    return data


if __name__ == "__main__":
    # data内容为response返回内容
    data = '''{"errorCode":0,"errorMsg":"ok","data":{"data":[{"key":"184","name":"Te quiero, mamá","icon":"http://cdn.kikakeyboard.com/sticker_partnermother_s_day_3/56.png","icon_big":"http://cdn.kikakeyboard.com/sticker_partnermother_s_day_3/240.png","column_count":3,"stickers":[{"key":"a739d89595d56347251cac04a7dcd6e6","name":" \\r","tags":[],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnermother_s_day_3/1-mother_mika_01-min_2.gif","width":457,"height":270},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-picture/e2401fa6-a26d-41c3-862c-7f4c1fb51c24.webp","width":457,"height":270},"scale_type":0},{"key":"4d31fa78eef4a1d9e557cd48bfb99ded","name":" \\r","tags":[],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnermother_s_day_3/2-mother_mika_02-min.gif","width":458,"height":270},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-picture/785d1158-8979-42cc-9234-364e0343854f.webp","width":458,"height":270},"scale_type":0},{"key":"940044dc33286af08850b1b6530f5a09","name":" \\r","tags":[],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnermother_s_day_3/3-mother_mika_03-min.gif","width":458,"height":270},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-picture/c2ca2bf5-be9a-475f-b78b-efa11d6f556f.webp","width":458,"height":270},"scale_type":0},{"key":"43f4ca077590da48217e341e78aaf9fb","name":" \\r","tags":[],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnermother_s_day_3/4-Thank_you_Mom.png","width":458,"height":270},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-picture/de325835-3a72-4aeb-b10f-c76bf892db07.webp","width":458,"height":270},"scale_type":0},{"key":"7a65c1822cd23fd42a8ed2a59eed7355","name":" \\r","tags":[],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnermother_s_day_3/Feliz_Dia_das_Ma_es.png","width":458,"height":270},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-picture/8980a2eb-c447-4418-8f81-4c2612bd800b.webp","width":458,"height":270},"scale_type":0},{"key":"10bd4ef64c7d0e6cf17b86bbc598686f","name":" ","tags":[],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnermother_s_day_3/feliz_di_a_mami.png","width":458,"height":270},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-picture/fe61735e-1e78-46a4-91a7-d6fa537151c1.webp","width":458,"height":270},"scale_type":0}],"author":{"key":"","name":"","avatar":""},"description":"Thank you, Mom! Happy mother\'s day!"},{"key":"185","name":"TechSmartt","icon":"http://cdn.kikakeyboard.com/sticker_partnerYouTube_techsmartt/56.png","icon_big":"http://cdn.kikakeyboard.com/sticker_partnerYouTube_techsmartt/240.png","column_count":3,"stickers":[{"key":"6b72395c8c5cd099a35925805819726","name":"FidgetSpinner\\r","tags":["FidgetSpinner"],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnerYouTube_techsmartt/Fidget-Spinner.png","width":458,"height":270},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-picture/942b102c-2014-4bd4-ae5a-1838b5f6e145.webp","width":458,"height":270},"scale_type":0},{"key":"c71402f5605d4e032a4ae15fbc36f5b4","name":"Laugh\\r","tags":["Laugh"],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnerYouTube_techsmartt/Laugh-with-tears.png","width":458,"height":270},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-picture/fe555a1e-cf6f-4369-83d9-aa9cb5593e82.webp","width":458,"height":270},"scale_type":0},{"key":"2dd2d54133dc7e9f691cb2ff97531340","name":"LOL\\r","tags":["LOL"],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnerYouTube_techsmartt/Lol.png","width":458,"height":270},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-picture/08a38847-0734-4361-a89e-11b204cb9aac.webp","width":458,"height":270},"scale_type":0},{"key":"d8a34cf91bda64034f46d31102ae9580","name":"OK\\r","tags":["OK"],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnerYouTube_techsmartt/OK.png","width":458,"height":270},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-picture/294a79ec-73b5-42f5-ad37-274166251866.webp","width":458,"height":270},"scale_type":0},{"key":"86b659329ff60776fa221b0cf692f573","name":"Peace\\r","tags":["Peace"],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnerYouTube_techsmartt/Peace.png","width":458,"height":270},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-picture/3b789dd5-cce4-404a-8a88-e63a963a373d.webp","width":458,"height":270},"scale_type":0},{"key":"d1cfcebe168db62a47c6696dce64c550","name":"Sup\\r","tags":["Sup"],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnerYouTube_techsmartt/Sup.png","width":458,"height":270},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-picture/a70c0642-c170-4008-b9d2-151e71d9a3d2.webp","width":458,"height":270},"scale_type":0},{"key":"bdd6c8703d53ca5a9a6f8ffc3e968107","name":"ThumbsDown\\r","tags":["ThumbsDown"],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnerYouTube_techsmartt/Thumbs-Down.png","width":458,"height":270},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-picture/8b4da73a-5f1e-4069-a3a4-25e46d2c24bd.webp","width":458,"height":270},"scale_type":0},{"key":"97c414487d5b6de7714f2ed9fa96a124","name":"ThumbsUp\\r","tags":["ThumbsUp"],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnerYouTube_techsmartt/Thumbs-Up.png","width":458,"height":270},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-picture/eeebc5bd-3660-4723-9326-9eb80c9bba87.webp","width":458,"height":270},"scale_type":0},{"key":"3ba8bce3a54fc96414813af835cdabf7","name":"Wow ","tags":["Wow"],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnerYouTube_techsmartt/Wow.png","width":458,"height":270},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-picture/fdda7b3e-1476-4226-b254-2bd8ea38d19f.webp","width":458,"height":270},"scale_type":0}],"author":{"key":"","name":"","avatar":""},"description":"Download and share the stickers from the popular YouTube channel! youtube.com/user/TechSmartt"},{"key":"181","name":"Funny Dogs Perros Divertidos","icon":"http://cdn.kikakeyboard.com/sticker_partnerDog_from_online/56.png","icon_big":"http://cdn.kikakeyboard.com/sticker_partnerDog_from_online/240.png","column_count":3,"stickers":[{"key":"3ee99c4e94b63fdb47281367caacb806","name":" \\r","tags":[],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnerDog_from_online/file_11409092.jpg","width":512,"height":512},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-content-sending/3232fff1-9486-4532-b5c3-92be305e5e35.webp","width":512,"height":512},"scale_type":0},{"key":"5ad4d1870ef0d5c441dbf2be544ed59b","name":" \\r","tags":[],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnerDog_from_online/file_11409093.jpg","width":512,"height":512},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-content-sending/555f0130-4a84-4570-844e-87a2bca90cc2.webp","width":512,"height":512},"scale_type":0},{"key":"efa7db37472471bc9ae321090c3a090a","name":" \\r","tags":[],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnerDog_from_online/file_11409098.jpg","width":512,"height":512},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-content-sending/86e7750d-5973-44bc-b5fc-5761b1fa252f.webp","width":512,"height":512},"scale_type":0},{"key":"82273503223c3a8bc15189cb3bbe19dd","name":" \\r","tags":[],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnerDog_from_online/file_11409099.jpg","width":512,"height":512},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-content-sending/7ab99972-2716-4e02-a1c8-4ebad59d2a67.webp","width":512,"height":512},"scale_type":0},{"key":"e67e4c621980998925f9ee1300b195ce","name":" \\r","tags":[],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnerDog_from_online/file_11409103.jpg","width":512,"height":512},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-content-sending/3e64beb7-0d26-47bf-8d29-079211d97c71.webp","width":512,"height":512},"scale_type":0},{"key":"6466c1b09491cc5d4908e6629da4af22","name":" \\r","tags":[],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnerDog_from_online/file_11409108.jpg","width":512,"height":512},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-content-sending/38783288-12e6-4f0a-b96b-9f341963f086.webp","width":512,"height":512},"scale_type":0},{"key":"569cc56b8d646679e5da06c5f1cc5992","name":" \\r","tags":[],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnerDog_from_online/file_11409112.jpg","width":512,"height":512},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-content-sending/9d84740a-85cf-4b1f-a664-6d94cd447f18.webp","width":512,"height":512},"scale_type":0},{"key":"60826011dcbfa2ef6e3a328abb9dc0d6","name":" \\r","tags":[],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnerDog_from_online/file_11409113.jpg","width":512,"height":512},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-content-sending/a60203a6-578f-4408-b616-86bdc8fac262.webp","width":512,"height":512},"scale_type":0},{"key":"f5a98ddcfe8aee4f8a56e7b02efeb55a","name":" \\r","tags":[],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnerDog_from_online/file_11409115.jpg","width":512,"height":512},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-content-sending/5572b3a0-0519-4f03-8890-91383c84e423.webp","width":512,"height":512},"scale_type":0},{"key":"26963bf7e8a72f774c6ba1d935d020ec","name":" \\r","tags":[],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnerDog_from_online/file_11409118.jpg","width":512,"height":512},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-content-sending/797cbe2b-6c7b-42ba-a41e-3d4b7f4ec9ce.webp","width":512,"height":512},"scale_type":0},{"key":"89b0a21f127569adf69e305d4eaf888","name":" \\r","tags":[],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnerDog_from_online/file_11409124.jpg","width":512,"height":512},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-content-sending/9169e419-cf4c-4713-92f7-8ec6a61c5b96.webp","width":512,"height":512},"scale_type":0},{"key":"6cef21d9cf5d3dcc7dd426d26ed703d","name":" \\r","tags":[],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnerDog_from_online/file_11409125.jpg","width":512,"height":512},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-content-sending/386baa86-ccba-4508-9a4b-3e9229b475c7.webp","width":512,"height":512},"scale_type":0},{"key":"6abcf87d5f42875bf03085bc31dc874a","name":" \\r","tags":[],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnerDog_from_online/file_11409130.jpg","width":512,"height":512},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-content-sending/c7d6a478-ebf6-469b-954b-1d5a60807eef.webp","width":512,"height":512},"scale_type":0},{"key":"f8b7878da4e530e5056865df5b262593","name":" \\r","tags":[],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnerDog_from_online/file_11409131.jpg","width":512,"height":512},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-content-sending/3f5bf944-1daf-426f-b507-a5c53208de57.webp","width":512,"height":512},"scale_type":0},{"key":"1e4a2ee304c50d33a1decece8e92c875","name":" \\r","tags":[],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnerDog_from_online/file_11409136.jpg","width":512,"height":512},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-content-sending/fd7345cd-06eb-434b-bdf2-6faaecda1d8c.webp","width":512,"height":512},"scale_type":0},{"key":"522ef6be083b2fd4a929644b5bf714fe","name":" \\r","tags":[],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnerDog_from_online/file_11409139.jpg","width":512,"height":512},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-content-sending/20575025-2299-4a18-94ef-ea3651988a50.webp","width":512,"height":512},"scale_type":0},{"key":"8f9a3d87fe0a245bd3f0039ceebffddd","name":" \\r","tags":[],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnerDog_from_online/file_11409148.jpg","width":512,"height":512},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-content-sending/efa20820-ddef-43b6-b31e-163f1b453364.webp","width":512,"height":512},"scale_type":0},{"key":"b3183e8b41dc8ca3641931d2f3271cf6","name":" \\r","tags":[],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnerDog_from_online/file_11409157.jpg","width":512,"height":512},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-content-sending/8ffad244-c957-448f-9cb4-63841e2b956f.webp","width":512,"height":512},"scale_type":0},{"key":"5fa0167d8531ba05edd2ac745c2efe5f","name":" \\r","tags":[],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnerDog_from_online/file_11409158.jpg","width":512,"height":512},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-content-sending/533a6276-b439-4907-beef-944e15100ce0.webp","width":512,"height":512},"scale_type":0},{"key":"83e02a272103eb9c6654f8eaf99e7360","name":" \\r","tags":[],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnerDog_from_online/file_11409159.jpg","width":512,"height":512},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-content-sending/eb5512d9-59ec-4e23-8c62-20f0d5aa3943.webp","width":512,"height":512},"scale_type":0},{"key":"ae14dc2276b355b5a8037de6f5f5917f","name":" \\r","tags":[],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnerDog_from_online/file_11409161.jpg","width":512,"height":512},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-content-sending/ace258e1-7af2-4af9-9a27-82e2876a59d5.webp","width":512,"height":512},"scale_type":0},{"key":"cac066da0ac01abcfc61356eb37b92b2","name":" \\r","tags":[],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnerDog_from_online/file_11409162.jpg","width":512,"height":512},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-content-sending/d7c62df0-6e67-4887-b87d-4b8e531fe9e5.webp","width":512,"height":512},"scale_type":0},{"key":"a76a09268e71747640fcc0e1568f7f42","name":" \\r","tags":[],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnerDog_from_online/file_11409163.jpg","width":512,"height":512},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-content-sending/a0a6a9a2-4515-416b-a479-eaf7f1f2b050.webp","width":512,"height":512},"scale_type":0},{"key":"2d30f502290a78a5ec20507e0be86e3e","name":" ","tags":[],"type":1,"image":{"url":"http://cdn.kikakeyboard.com/sticker_partnerDog_from_online/file_11409165.jpg","width":512,"height":512},"mp4":null,"webp":{"url":"http://cdn.kikakeyboard.com/backend-content-sending/afdb32c0-2342-4305-acda-8babea5408ca.webp","width":512,"height":512},"scale_type":0}],"author":{"key":"","name":"","avatar":""},"description":"All pictures are collected from online, any problem pls contact: support@kikatech.com"}],"page":0,"size":3,"next_page":1}}'''
    print(data_clear(data))
