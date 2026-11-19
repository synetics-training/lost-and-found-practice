# 분실물 관리 서비스 - 코드 품질 실습용 
import os, sys
import datetime

items = []
NEXT_NO = 1

def RegisterItem(name,category,found_date,location,finder,memo):
    global NEXT_NO
    if name == None or name == "":
        return "물품명을 입력하세요"
    if category == None or category == "":
        return "분류를 입력하세요"
    l = len(name)
    item = {"no": "P" + str(NEXT_NO), "name": name, "category": category, "found_date": found_date, "location": location, "status": "보관 중"}
    items.append(item)
    NEXT_NO+=1
    return item["no"]

def search_by_name(keyword):
    result = [
        item["no"] + " " + item["name"]
        + " [" + item["category"] + "]"
        + " 습득일 " + item["found_date"]
        + " / 보관 장소 " + item["location"]
        for item in items
        if item["status"] == "보관 중" and keyword in item["name"]
    ]
    if len(result) == 0:
        print("검색 결과가 없습니다. 학생지원팀에 문의하세요.")
    return result

def search_by_category(keyword):
    result = []
    for item in items:
        is_stored = item["status"] == "보관 중"
        matches_category = is_stored and keyword in item["category"]
        if is_stored and matches_category:
            result.append(
                item["no"] + " " + item["name"]
                + " [" + item["category"] + "]"
                + " 습득일 " + item["found_date"]
                + " / 보관 장소 " + item["location"]
            )
    if len(result) == 0:
        print("검색 결과가 없습니다. 학생지원팀에 문의하세요.")
    return result

def _find_item(item_no):
    for item in items:
        if item["no"] == item_no:
            return item
    return None

def _handover_validation_error(owner_checked, today, staff):
    if owner_checked != True:
        return "주인 확인이 필요합니다"
    if today == None or today == "":
        return "인도일을 입력하세요"
    if staff == None or staff == "":
        return "담당자를 입력하세요"
    return None

def handover(item_no, owner_checked, today, staff):
    if item_no == None or item_no == "":
        return "물품 번호를 입력하세요"

    item = _find_item(item_no)
    if item == None:
        return "등록되지 않은 물품 번호입니다"
    if item["status"] == "보관 중":
        validation_error = _handover_validation_error(owner_checked, today, staff)
        if validation_error != None:
            return validation_error
        item["status"] = "인도 완료"
        item["handover_date"] = today
        item["staff"] = staff
        return "인도 완료"
    if item["status"] == "인도 완료":
        return "이미 인도된 물품입니다"
    return "알 수 없는 상태입니다"

def count_by_status():
    try:
        stored = len([i for i in items if i["status"] == "보관 중"])
        handed = len([i for i in items if i["status"] == "인도 완료"])
    except:
        return None
    return {"보관 중": stored, "인도 완료": handed}

if __name__ == "__main__":
    RegisterItem("검정 우산", "기타", "2026-11-12", "학생지원팀 보관함", "학생A", "")
    print(search_by_name("우산")); print(handover("P1", True, "2026-11-19", "담당자A"))
    print(count_by_status())
