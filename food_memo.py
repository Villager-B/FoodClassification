import pandas as pd
import pyto_ui as ui


view = ui.TextView()
view.background_color = ui.COLOR_SYSTEM_BACKGROUND
view.editable = True
view.font = ui.Font.system_font_of_size(20)
bitem = ui.ButtonItem(title='ShimaMemo')
bitem.enabled = False
view.button_items = [bitem]
ui.show_view(view, ui.PRESENTATION_MODE_SHEET)


memo_text = view.text

memo_text = memo_text.split('\n')
memo_text = memo_text[:len(memo_text)-1]
    

food_df = pd.read_csv("synonym_je.tsv",sep="\t",names=["大分類","総称","名称"], header=None)

food_set = set(food_df["大分類"].tolist())
result_dic = dict()
food_list = list(food_set)

for category in food_list:
    result_dic[category] = list()
result_dic["その他"] = list()

for food in memo_text:
    try:
        result_dic[food_df[food_df["名称"] == food]["大分類"].tolist()[0]].append(food)
    except:
        result_dic["その他"].append(food)
                
sort_result_text = ""

sort_result_text += "野菜🥦 : \n"
for item in result_dic["材料-野菜"]:
    sort_result_text += item+"\n"
sort_result_text += "\n魚介🍤 : \n"
for item in result_dic["材料-魚介"]:
    sort_result_text += item+"\n"
sort_result_text += "\n肉🍖 : \n"
for item in result_dic["材料-肉"]:
    sort_result_text += item+"\n"
sort_result_text += "\n調味料🧂 : \n"
for item in result_dic["調味料"]:
    sort_result_text += item+"\n"
sort_result_text += "\n材料その他🍳 : \n"
for item in result_dic["材料-その他"]:
    sort_result_text += item+"\n"
sort_result_text += "\nその他 : \n"
for item in result_dic["その他"]:
    sort_result_text += item+"\n"


rview = ui.TextView()
rview.background_color = ui.COLOR_SYSTEM_BACKGROUND
rview.text = sort_result_text
rview.editable = False
rview.font = ui.Font.system_font_of_size(20)
bitem = ui.ButtonItem(title='ShimaMemo Result')
bitem.enabled = False
rview.button_items = [bitem]
ui.show_view(rview, ui.PRESENTATION_MODE_SHEET)

