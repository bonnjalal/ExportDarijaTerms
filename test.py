from queue import Empty
import re
import json
# import xlwings
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment  
import openpyxl
import copy

with open('test.json') as json_file:
    data = json.load(json_file)
     
        # Print the type of data variable
        # print(data)

wb = Workbook()  
ws = wb.active
# wb1.save('test.xlsx')
# wb = load_workbook('test.xlsx', data_only=True)
# ws = wb.active 

def depth(d):
    if isinstance(d, dict):
        return 1 + (max(map(depth, d.values())) if d else 0)
    return 0

# def openCloseXl():
#     excel_app = xlwings.Book()
#     excel_book = excel_app.books.open('test.xlsx')
#     excel_book.save()
#     excel_book.close()
#     excel_app.quit()

def getMergedCellVal(sheet, cell):
    rng = [s for s in sheet.merged_cells.ranges if cell.coordinate in s]
    return sheet.cell(rng[0].min_row, rng[0].min_col).value if len(rng)!=0 else cell.value

def getValueWithMergeLookup(cell):
    idx = cell.coordinate

    # for range_ in sheet.merged_cell_ranges:
    # 'merged_cell_ranges' has been deprecated
    # 'merged_cells.ranges' should be used instead
    for range_ in ws.merged_cells.ranges:

        # merged_cells = list(openpyxl.utils.rows_from_range(range_))
        # 'rows_from_range' should take a 'str' type argument
        merged_cells = list(openpyxl.utils.rows_from_range(str(range_)))

        for row in merged_cells:
            if idx in row:
                # If this is a merged cell,
                # return  the first cell of the merge range

                # return sheet.cell(merged_cells[0][0]).value
                # You can just use 'sheet[<CELL ADDRESS>]' to take a cell
                # ex) sheet["A1"].value

                value = ws[merged_cells[0][0]].value
                # print("value >>>>> " + str(ws[merged_cells[0][0]].value))
                return value
                # return row.start_cell.value

    # return sheet.cell(idx).value
    return ws[idx].value

def wordfinder2(searchString:str, rngr:list, rngc:list):
    rowrng = range(rngr[0], rngr[1]+1)  
    colrng = range(rngc[0], rngc[1]+1)
    # print("rowrng" + str(rowrng))
    # print("colrng" + str(colrng))
    # for i in range(1, ws.max_row + 1):
    print("serching for: " + searchString)
    for i in rowrng:
        # for j in range(1, 6 + 1):
        for j in colrng:
            # print("wordFinder: " + str(sheet.cell(row=i,column=j).value))
            cell = ws.cell(row=i,column=j)
            strValue = cell.value
            if type(cell) == openpyxl.cell.cell.MergedCell:
                coord = cell.coordinate
                strValue = getValueWithMergeLookup(cell)
                print(strValue)

            if searchString == strValue:
                print("found found found found found ")
                return i,j
    return -1,-1

def wordfinder(searchString:str, rngr:list, rngc:list):
    # rowrng = range(rngr[0], rngr[1]+1)  
    # colrng = range(rngc[0], rngc[1]+1)

    print("serching for: " + searchString)
    
    # print(rngr[0])
    for row in ws.iter_cols(min_row=rngr[0], min_col=rngc[0], max_row=rngr[1], max_col=rngc[1]):  
        for cell in row:  
            # print("wordFinder: " + str(cell.value))
            strValue = cell.value 
            if type(cell) == openpyxl.cell.cell.MergedCell:
                coord = cell.coordinate
                strValue = getValueWithMergeLookup(cell)
                # print("strVal: " + str(strValue))
            if searchString == strValue:
                print("found found found found found ")
                return cell.row,cell.column

            # print(cell.value, end=" ")
    return -1,-1

def getMergedCellRange(cell):
    # for merged_cells in ws.merged_cells:
    #     if(merged_cells.start_cell.value != None):
    #         print(f"Merged Cell {merged_cells.coord} value is {merged_cells.start_cell.value}")
#
    rng = [s for s in ws.merged_cells.ranges if cell.coordinate in s]
    # return sheet.cell(rng[0].min_row, rng[0].min_col).value if len(rng)!=0 else cell.value
    if len(rng) != 0:
        return [rng[0].min_row, rng[0].max_row], [rng[0].min_col, rng[0].max_col]

    return [cell.row, cell.row], [cell.column, cell.column]
    # return range(rng[0].min_row, rng[0].max_row), range(rng[0].min_col, rng[0].max_col) if len(rng) != 0 else range(cell.row, cell.row), range(cell.column, cell.column)

def cellEmpty(cell):
    # value = getValueWithMergeLookup(cell)
    value = cell.value
    if type(cell) == openpyxl.cell.cell.MergedCell:
        return False
    if value is None or value == "":
        return True
    return False

# mrgList = []
# dp = 1
def insertCell2(data,crow , ranger:list, rangec:list, mergeList:list, depth1):
    # wb = load_workbook('test.xlsx', data_only=True)
    # ws = wb.active 
 
    rngr = ranger
    rngc = rangec

    # ranger = []
    # rangec = []

    d = 0

    mrgList = mergeList

    dp = depth1
    sRngList = [2]
    # rngr[0] = dp
    # rngr[1] = dp

    rngc1 = rngc
    for it2 in data:
        # print(it2)
        # print(mrgList)
        # print("start row__: " + str(rngr))
        # Etymology 1
       
        # print("rngr before: " + str(rngr))
        row2,col2 = wordfinder(it2, rngr, rngc)
        # print("word: " + str(row2) + str(col2))

        # maxCol = ws.max_column
        if row2 == -1:
            maxCol = rngc[1]
            row2 = dp
            cCell =ws.cell(row=row2, column=maxCol)
            # print("cCell : " + str(cCell))
            # print("MaxCol before empty : " + str(maxCol))
            if not cellEmpty(cCell):
                # print("not empty")
                maxCol += 1
                ws.insert_cols(idx=maxCol)
            # sRngList[dp-1] = maxCol
            rngc1[0] = maxCol
            # print("MaxCol after empty : " + str(maxCol))
            
            # maxCol= ws.max_column
            # row2 = rngr[0]
            
            col2 = maxCol
            # print("rngr 0 : " + str(rngr[0]))
            # ws.cell(row=row2, column=col2).value = it2
           

            mrgListlen = len(mrgList)
            # print("mrg liat len: " + str(mrgListlen))
            
            if(mrgListlen >= row2):
                for r in range(mrgListlen -(row2-1)):
                    mrgList.pop(mrgListlen-1-r)
                    # print("poped : "+str(mrgList))
                    # mrgList[row2-1] = [rngr, rngc]

            for r in range(len(mrgList)):
                mrgList[r][1][1] = col2
                print(mrgList[r])

                # if mrgList[r][1][0] != col2:
                    # print(" /row start " + str(mrgList[r][0][0]) + " /col start " + str(mrgList[r][1][0]) + " /row end " + str(mrgList[r][0][1]) + " /col end " + str(col2))
                    # try:
                    #     ws.unmerge_cells(start_row=mrgList[r][0][0], start_column=mrgList[r][1][0],
                    #                end_row=mrgList[r][0][1], end_column=mrgList[r][1][1])
                    # except :
                    #     print("not merged")
                    #   
                    #
                    # ws.merge_cells(start_row=mrgList[r][0][0], start_column=mrgList[r][1][0],
                    #                end_row=mrgList[r][0][1], end_column=col2)  

                    # mrgList[r][1][1] = col2

                    # rng1, rng2 = getMergedCellRange(ws.cell(row=mrgList[r][0][0], column=mrgList[r][1][0]))
                    #
                    # print("New Merge List: " + str(rng1) + " / " + str(rng2))
                    # 
                    # # print(mrgList[r])
                    #
                    # cell = ws.cell(row=mrgList[r][0][0], column=mrgList[r][1][0])  
                    # # print(mrgRange)
                    # # cell.value = 'Devansh Sharma'  
                    # cell.alignment = Alignment(horizontal='center', vertical='center') 

            ws.cell(row=row2, column=col2).value = it2

            mrgListlen = len(mrgList)
            # print("mrgList len after pop >>>>>>>>>>>>>>>>>>>>" +str(mrgListlen))

        
            if(mrgListlen > row2):
                for r in range(mrgListlen - row2):
                    mrgList.pop(mrgListlen-1-r)
                # rngc[0] = sRngList[dp-1]
                mrgList[row2-1] = [rngr, rngc]
                # mrgList[row2-1] = [rngr, rngc]
                
                    
            elif(mrgListlen == row2):
                mrgList[row2-1] = [rngr, rngc]
            else:
                mrgList.append([rngr,rngc])


            rngr = mrgList[dp-1][0]
            rngc = mrgList[dp-1][1]



        # return range2r and range2c
        # print("row2 = " + str(row2) + "/ col 2 = " + str(col2))
        # rngr, rngc = getMergedCellRange(ws.cell(row= row2, column=col2))
        # print("mergedCells" + str(rngr) + str(rngc) + " dp: " +str(dp))
        # print("start col:" + str(row2) + " start row: " + str(row2) )
        

        

        if depth(data[it2]) <= d:
            value = data[it2]
            if (type(value) == list):
                value = ', '.join([str(elem) for elem in value])
            ws.cell(row=crow, column=col2).value = value
            # mrgList.clear()
            # wb.save("test.xlsx")
            # openCloseXl()
        else:
            # wb.save("test.xlsx")
            # openCloseXl()
            # rngr, rngc = insertCell(data[it2], crow, rngr, rngc, mrgList, dp+1)
            insertCell(data[it2], crow, rngr, rngc, mrgList, dp+1)

    # return rngr, rngc

rangeList = [[[1,1],[2,2]]]
# rangeDict = {}
countEnter = 0
countExit = 0
count = [0,0]

def insertCell3(data, crow, depth1):

    d = 0

    dp = depth1
  
    for it2 in data:

        # print("search range" + str([dp,dp]) + " / " + str(rangeList[dp-1][1]))
        row1,col1 = wordfinder(it2, [dp,dp], rangeList[dp-1][1])
        row2 = dp
        # col2 = rangeList[dp-1][1][1]
        col2 = col1

        if row1 == -1:
            maxCol = rangeList[dp-1][1][1]
            col1 = rangeList[dp-1][1][0]

            # row2 = dp
            cCell = ws.cell(row=row2, column=maxCol)

            if not cellEmpty(cCell):
                maxCol += 1
                # ws.insert_cols(idx=maxCol)
                col1 = maxCol

            col2 = maxCol

            # mKeyCol = maxCol
            keyCol = maxCol

            dataKeys = list(data.keys())
            # print("datakeys " + str(dataKeys[0]))
            for k in range(len(dataKeys)):
                kRow,kCol = wordfinder(dataKeys[k], [dp,dp], rangeList[dp-1][1])
                if (kRow == -1):
                    kCell = ws.cell(row=row2, column=keyCol)
                    if not cellEmpty(kCell):
                        keyCol +=1
                        ws.insert_cols(idx=keyCol)
                    ws.cell(row=row2, column=keyCol).value = dataKeys[k]
        
            for r in range(dp):
                print("enter List : " + str(rangeList[r]))
                rangeList[r][1][1] = keyCol
            
            

            # print("col 1: " + col1)

        rngr = [dp, dp]
        rngc = [col1, col2]
        
        # print("range c after : " + str(rngc))
        try: 
            rangeList[dp] = [rngr, rngc, it2]
        except:
            rangeList.append([rngr,rngc, it2])

        # rangeList[0][1][1] = ws.max_column
            
            
        print("Exit List : " + str(rangeList))

        # rngr, rngc = getMergedCellRange(ws.cell(row= row2, column=col2))
        

        if depth(data[it2]) <= d:
            value = data[it2]
            if (type(value) == list):
                value = ', '.join([str(elem) for elem in value])
            ws.cell(row=crow, column=col2).value = value
        else:
            insertCell(data[it2], crow, dp+1)


def insertCell4(data, crow, depth1):

    count[0] += 1
    count[1] -= 1
    # countEnter +=1
    # countExit -=1
    
    d = 0

    # mrgList = mergeList

    dp = depth1

    tmpRngList = copy.deepcopy(rangeList)
    # print("id list: " + str(id(rangeList)))
    # print("id copy list: " + str(id(tmpRngList)))
    # rngr = tmpRngList[dp-1][0]
    # rngr = [dp, dp] 
    # rngc = tmpRngList[dp-1][1]
    
    isEntringFun = True
   
    insertCol = True
  
    for it2 in data:

        
        # print("search range" + str([dp,dp]) + " / " + str(rangeList[dp-1][1]))
        row2,col2 = wordfinder(it2, [dp,dp], rangeList[dp-1][1])
        col1 = rangeList[dp-1][1][0]

        

        
        if row2 == -1:
            maxCol = rangeList[dp-1][1][1]
            row2 = dp
            cCell = ws.cell(row=row2, column=maxCol)

                        # print("cCell : " + str(cCell))
            # print("MaxCol before empty : " + str(maxCol))
            print("lenth range: " + str(len(rangeList)) + " dp " + str(dp))
            if not cellEmpty(cCell) or not insertCol:
            # if not cellEmpty(cCell) or count[1] >= count[0]:
                # print("not empty")
                maxCol += 1
                ws.insert_cols(idx=maxCol)
                col1 = maxCol
            # if col1 == maxCol and cellEmpty(cCell):
            #     maxCol = maxCol
            # else:
            #     maxCol += 1
            #     ws.insert_cols(idx=maxCol)
            #     col1 = maxCol
            
            # print("range c before : " + str(rngc))
            # rngc[0] = maxCol
                # print("search range after " + str(rngr) + " / " + str(rngc))
            
            
            
            
            col2 = maxCol

            # mrgListlen = len(rangeList)
            
            # if(mrgListlen > row2):
            #     for r in range(mrgListlen -(row2-1)):
            #         mrgList.pop(mrgListlen-1-r)

            for r in range(dp):
                print("enter List : " + str(rangeList[r]))
                rangeList[r][1][1] = col2
            # for r in range(dp):
            #     rangeList[r][1][1] = col2

                # if mrgList[r][1][0] != col2:
                    # print(" /row start " + str(mrgList[r][0][0]) + " /col start " + str(mrgList[r][1][0]) + " /row end " + str(mrgList[r][0][1]) + " /col end " + str(col2))
                    # try:
                    #     ws.unmerge_cells(start_row=mrgList[r][0][0], start_column=mrgList[r][1][0],
                    #                end_row=mrgList[r][0][1], end_column=mrgList[r][1][1])
                    # except :
                    #     print("not merged")
                    #   
                    #
                    # ws.merge_cells(start_row=mrgList[r][0][0], start_column=mrgList[r][1][0],
                    #                end_row=mrgList[r][0][1], end_column=col2)  

                    # mrgList[r][1][1] = col2

                    # rng1, rng2 = getMergedCellRange(ws.cell(row=mrgList[r][0][0], column=mrgList[r][1][0]))
                    #
                    # print("New Merge List: " + str(rng1) + " / " + str(rng2))
                    # 
                    # # print(mrgList[r])
                    #
                    # cell = ws.cell(row=mrgList[r][0][0], column=mrgList[r][1][0])  
                    # # print(mrgRange)
                    # # cell.value = 'Devansh Sharma'  
                    # cell.alignment = Alignment(horizontal='center', vertical='center') 

            ws.cell(row=row2, column=col2).value = it2
        
        rngr = [dp, dp]
        rngc = [col1, col2]
        
        # print("range c after : " + str(rngc))
        try: 
            rangeList[dp] = [rngr, rngc]
        except:
            rangeList.append([rngr,rngc])
            
            
        print("Exit List : " + str(rangeList))


            # mrgListlen = len(rangeList)
    
            # try: 
            #     rangeList[dp] = [rngr, rngc]
            # except:
            #     rangeList.append([rngr,rngc])

            #
            # rngr = mrgList[dp-1][0]
            # rngc = mrgList[dp-1][1]



        # rngr, rngc = getMergedCellRange(ws.cell(row= row2, column=col2))
        

        if depth(data[it2]) <= d:
            value = data[it2]
            if (type(value) == list):
                value = ', '.join([str(elem) for elem in value])
            ws.cell(row=crow, column=col2).value = value
        else:
            insertCell(data[it2], crow, dp+1)

        insertCol = False

    count[0] -= 1
    count[1] += 1


def nested_get(dic, keys):
    dic2 = copy.deepcopy(dic)
    for key in keys:
        dic2 = dic2[key]
    return dic2

def nested_set(dic, keys, value):
    for key in keys[:-1]:
        dic = dic.setdefault(key, {})
    dic[keys[-1]] = value

def nested_del(dic, keys):
    for key in keys[:-1]:
        dic = dic[key]
    del dic[keys[-1]]

rangesDict = {"word": {"rng" : [[1,1],[2,2]]}}
keysList = ["word"]
def insertCell(data, crow, depth1):
    # print(rangesDict)
    # countEnter +=1
    # countExit -=1
    
    d = 0

    # mrgList = mergeList

    dp = depth1

    # tmpRngList = copy.deepcopy(rangeList)
    # print("id list: " + str(id(rangeList)))
    # print("id copy list: " + str(id(tmpRngList)))
    # rngr = tmpRngList[dp-1][0]
    # rngr = [dp, dp] 
    # rngc = tmpRngList[dp-1][1]
    
    # isEntringFun = True
   
    insertCol = True
  
    for it2 in data:

        
        
        tmpKeysList1 = []
        for i in range(dp):
            tmpKeysList1.append(keysList[i])
        # tmpKeysList1.append("rng")

        rng = nested_get(rangesDict, tmpKeysList1+["rng"]) 
        
        row2,col1 = wordfinder(it2, [dp,dp], rng[1])
        print(tmpKeysList1)
        print("search range col: " + str(rng[1]) + " dp " + str(dp))
        col2 = col1
        
        if row2 == -1:
            col1 = rng[1][0]
            maxCol = rng[1][1]
            row2 = dp
            cCell = ws.cell(row=row2, column=maxCol)

                        # print("cCell : " + str(cCell))
            # print("MaxCol before empty : " + str(maxCol))
            # print("lenth range: " + str(len(rangeList)) + " dp " + str(dp))
            if not cellEmpty(cCell) or not insertCol:
            # if not cellEmpty(cCell) or count[1] >= count[0]:
                # print("not empty")
                maxCol += 1
                ws.insert_cols(idx=maxCol)
                col1 = maxCol
            # if col1 == maxCol and cellEmpty(cCell):
            #     maxCol = maxCol
            # else:
            #     maxCol += 1
            #     ws.insert_cols(idx=maxCol)
            #     col1 = maxCol
            
            # print("range c before : " + str(rngc))
            # rngc[0] = maxCol
                # print("search range after " + str(rngr) + " / " + str(rngc))
            
            
            
            
            col2 = maxCol

            # mrgListlen = len(rangeList)
            
            # if(mrgListlen > row2):
            #     for r in range(mrgListlen -(row2-1)):
            #         mrgList.pop(mrgListlen-1-r)

            # tmpDict = copy.deepcopy(rangesDict)  
            # tmp2Dict = dict 
            keysListTmp = [] 
            for r in range(dp):
                if r == 0:
                    keysListTmp.append(keysList[r])
                    # keysListWRng = copy.deepcopy(keysListTmp)
                    # keysListWRng.append("rng")
                    tmpRng = nested_get(rangesDict, keysListTmp + ["rng"])
                    tmpRng[1][1] = ws.max_column + 1
                    nested_set(rangesDict, keysListTmp + ["rng"], tmpRng) 
                else:
                    keysListTmp.append(keysList[r])
                    # keysListWRng = copy.deepcopy(keysListTmp)
                    # keysListWRng.append("rng")
                    tmpRng = nested_get(rangesDict, keysListTmp + ["rng"])
                    tmpRng[1][1]= col2
                    nested_set(rangesDict, keysListTmp + ["rng"], tmpRng) 

                 ##### for debuging
                dDict = nested_get(rangesDict, keysListTmp + ["rng"])
                # print("#### " + str(keysList[r]) +" #### | " + str(dDict))
                # rangeList[r][1][1] = col2
            # for r in range(dp):
            #     rangeList[r][1][1] = col2

                # if mrgList[r][1][0] != col2:
                    # print(" /row start " + str(mrgList[r][0][0]) + " /col start " + str(mrgList[r][1][0]) + " /row end " + str(mrgList[r][0][1]) + " /col end " + str(col2))
                    # try:
                    #     ws.unmerge_cells(start_row=mrgList[r][0][0], start_column=mrgList[r][1][0],
                    #                end_row=mrgList[r][0][1], end_column=mrgList[r][1][1])
                    # except :
                    #     print("not merged")
                    #   
                    #
                    # ws.merge_cells(start_row=mrgList[r][0][0], start_column=mrgList[r][1][0],
                    #                end_row=mrgList[r][0][1], end_column=col2)  

                    # mrgList[r][1][1] = col2

                    # rng1, rng2 = getMergedCellRange(ws.cell(row=mrgList[r][0][0], column=mrgList[r][1][0]))
                    #
                    # print("New Merge List: " + str(rng1) + " / " + str(rng2))
                    # 
                    # # print(mrgList[r])
                    #
                    # cell = ws.cell(row=mrgList[r][0][0], column=mrgList[r][1][0])  
                    # # print(mrgRange)
                    # # cell.value = 'Devansh Sharma'  
                    # cell.alignment = Alignment(horizontal='center', vertical='center') 

            ws.cell(row=row2, column=col2).value = it2
        
            rngr = [dp, dp]
            rngc = [col1, col2]
            
            # print("range c after : " + str(rngc))

            tmpKeysList1.append(it2)
            tmpKeysList1.append("rng")
            nested_set(rangesDict, tmpKeysList1, [rngr, rngc])
        else:
            it2rng = nested_get(rangesDict, tmpKeysList1+[it2,"rng"])
            diffrence = col1 - it2rng[1][0]
            tmpRng = [it2rng[0], [it2rng[1][0]+diffrence ,it2rng[1][1]+diffrence]]

            nested_set(rangesDict, tmpKeysList1+[it2,"rng"], tmpRng)
            
            



            # rangesDict["word"]["rng"] = [[1,1],[2,ws.max_column]]
        try: 
            keysList[dp] = it2
        except:
            keysList.append(it2)
            
            
        # print("Exit Dict : " + str(rangesDict))


            # mrgListlen = len(rangeList)
    
            # try: 
            #     rangeList[dp] = [rngr, rngc]
            # except:
            #     rangeList.append([rngr,rngc])

            #
            # rngr = mrgList[dp-1][0]
            # rngc = mrgList[dp-1][1]



        # rngr, rngc = getMergedCellRange(ws.cell(row= row2, column=col2))
        

        if depth(data[it2]) <= d:
            value = data[it2]
            if (type(value) == list):
                value = ', '.join([str(elem) for elem in value])
            ws.cell(row=crow, column=col1).value = value
        else:
            insertCell(data[it2], crow, dp+1)

        insertCol = False

def insertData():
    axisr = [1,1]
    range2r = range(2,3)
    range3r = range(3,4)
    range4r = range(4,5)
    range5r = range(5,6)

    axisc = [2, ws.max_column]
    if ws.max_column <=1:
        axisc = [2, 2]

    mrgList = [[axisr, axisc]]
    
    # range2c = range(1, ws1.max_column +1)
    # range3c = range(1, ws1.max_column +1)
    # range4c = range(1, ws1.max_column +1)
    # range5c = range(1, ws1.max_column +1)

    crow = 5
    ccol = 2
    maxCol = ws.max_column
    d = 0
    for it in data.keys():
        print(rangesDict)
        
        # word name
        crow+=1
        # ccol+=1
        ws.cell(row=crow, column=1).value = it
        # wb1.save("test.xlsx")
        # rangesDict[keysList[0]]["rng"] = [[1,1],[2, ws.max_column]]

        insertCell(data[it], crow, 1)
        # insertCell(data[it], crow, axisr, axisc, [], 1)

def insertData2():
    range1r = range(1, ws.max_row + 1)
    range2r = range(1, ws.max_row + 1)
    range3r = range(1, ws.max_row + 1)
    range4r = range(1, ws.max_row + 1)
    range5r = range(1, ws.max_row + 1)
    range1r = range(1, ws.max_row + 1)

    range1c = range(1, 1)
    range2c = range(2, 2)
    range3c = range(3, 3)
    range4c = range(4, 4)
    range5c = range(5, 5)

    crow = 5
    ccol = 2
    # maxCol = 2
    d = 0
    for it in data.keys():
        # word name
        crow+=1
        # ccol+=1
        ws.cell(row=crow, column=1).value = it
        for it2 in data[it]:
            print(it2)
            # Etymology 1
            row2,col2 = wordfinder(it2, range1r, range1c)

            maxCol = ws.max_column
            if row2 == -1:
                ws.insert_cols(idx=maxCol+1)
                ws.cell(row=1, column=maxCol+1).value = it2
                maxCol= ws.max_column
                row2 = 1
                col2 = maxCol

                # ccol +=1

                # cell = ws.cell(row=1, column=ccol)
                # if cellEmpty(cell):
                #     cell.value = it2
                # else:
                #     ws.insert_cols(idx=ccol+1)
                #     ws.cell(row=1, column=ccol+3).value = it2
                #     ccol +=1

            if depth(data[it][it2]) <= d:
                value = data[it][it2]
                if (type(value) == list):
                    value = ', '.join([str(elem) for elem in value])
                ws.cell(row=crow, column=col2).value = value
            
            range2r, range2c = getMergedCellRange(ws, ws.cell(row= row2, column=col2))


             
            for it3 in data[it][it2]:
                # pronunciation        
                row3,col3 = wordfinder(it3)
                if row3 == -1:
                    cell = ws.cell(row=2, column=ccol)
                    if cellEmpty(cell):
                        cell.value = it3
                    else:
                        ws.insert_cols(idx=ccol+1)
                        ws.cell(row=2, column=ccol+1).value = it3
                        ccol +=1
                    if depth(data[it][it2][it3]) <= d:
                        value = data[it][it2][it3]
                        if ( type(value)== list):
                            value = ', '.join([str(elem) for elem in value])
                        ws.cell(row=crow, column=ccol).value = value
                        break

                else:
                    if depth(data[it][it2][it3]) <= d:
                        value = data[it][it2][it3]
                        if (type(value) == list):
                            value = ', '.join([str(elem) for elem in value])
                        ws.cell(row=crow, column=col3).value = value
                        break

                for it4 in data[it][it2][it3]:
                    # pron_text
                    row4,col4 = wordfinder(it4)
                    if row4 == -1:
                        cell = ws.cell(row=3, column=ccol)
                        if cellEmpty(cell):
                            cell.value = it4
                        else:
                            ws.insert_cols(idx=ccol+1)
                            ws.cell(row=3, column=ccol+1).value = it4
                            ccol +=1
                        print("it4 = " + it4)
                        print("it4 val " + str(data[it][it2][it3][it4]))
                        print("depth it4 " + str(depth(data[it][it2][it3][it4])))
                        if depth(data[it][it2][it3][it4]) <= d:
                            value = data[it][it2][it3][it4]
                            print("it4 value : " + str(data[it][it2][it3][it4]))
                            if (type(value) == list):
                                value = ', '.join([str(elem) for elem in value])
                            ws.cell(row=crow, column=ccol).value = value
                            break

                    else:
                        if depth(data[it][it2][it3][it4]) <= d:
                            value = data[it][it2][it3][it4]
                            if (type(value) == list):
                                value = ', '.join([str(elem) for elem in value])
                            ws.cell(row=crow, column=col4).value = value
                            break

                    for it5 in data[it][it2][it3][it4]:
                        # value
                        row5,col5 = wordfinder(it5)
                        print("it5 " + it5)
                        print("it5 value : " + str(data[it][it2][it3][it4][it5]))
                        if row5 == -1:
                            
                            cell = ws.cell(row=4, column=ccol)
                            if cellEmpty(cell):
                                cell.value = it5
                            else:
                                ws.insert_cols(idx=ccol+1)
                                ws.cell(row=4, column=ccol).value = it5
                                ccol +=1

                            if depth(data[it][it2][it3][it4][it5]) <= d:
                                
                                value = data[it][it2][it3][it4][it5]
                                if (type(value) == list):
                                    value = ', '.join([str(elem) for elem in value])
                                ws.cell(row=crow, column=ccol).value = value
                                break
                        else:
                            if depth(data[it][it2][it3][it4][it5]) <= d:
                                value = data[it][it2][it3][it4][it5]
                                if (type(value) == list):
                                    value = ', '.join([str(elem) for elem in value])
                                ws.cell(row=crow, column=col5).value = value
                                break

                        for it6 in data[it][it2][it3][it4][it5]:
                            # value
                            row6,col6 = wordfinder(it6)
                            if row6 == -1:
                                cell = ws.cell(row=5, column=ccol)
                                if cellEmpty(cell):
                                    cell.value = it6
                                else:
                                    ws.insert_cols(idx=ccol+1)
                                    ws.cell(row=5, column=ccol).value = it6
                                    ccol +=1
                                if depth(data[it][it2][it3][it4][it5][it6]) <= d:
                                    value = data[it][it2][it3][it4][it5][it6]
                                    if (type(value) == list):
                                        value = ', '.join([str(elem) for elem in value])
                                    ws.cell(row=crow, column=ccol).value = value
                                    break
                            else:
                                if depth(data[it][it2][it3][it4][it5][it6]) <= d:
                                    value = data[it][it2][it3][it4][it5][it6]
                                    if (type(value) == list):
                                        value = ' '.join([str(elem) for elem in value])
                                    ws.cell(row=crow, column=col6).value = value
                                    break


                    
    
        # i +=1
        

  
# sheet['A1'] = 87  
# sheet['A2'] = "Devansh"  
# sheet['A3'] = 41.80  
# sheet['A4'] = 10  
#   
# sheet.cell(row=2, column=2).value = 5  
#     # Print the data of dictionary
#     # print("\nPeople1:", data['people1'])
#     # print("\nPeople2:", data['people2'])
#
# # line = re.sub(r'[^\u0600-\u06FF]', '',input_str)
# ws.merge_cells('A2:B2')  
#   
# cell = ws.cell(row=2, column=1)  
# # cell.value = 'Devansh Sharma'  
# cell.alignment = Alignment(horizontal='center', vertical='center') 
#
#  
# ws.insert_cols(idx=2)



# print(j)

insertData()
wb.save("test.xlsx")  


# cell = ws.cell(row=1, column=2)

# print(getMergedCellVal(ws, cell))
