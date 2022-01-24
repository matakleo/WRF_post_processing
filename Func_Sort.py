from Func_List_Files import list_csv_files_3

##########################################
# This function sorts all the grid sizes.#
##########################################

def Sort_Grid_Sizes(Grid_Sizes):
  Sorted_Grid_Sizes = []
  Int_Grid_Sizes = []
  for Grid_Size in Grid_Sizes:
    idx = Grid_Size.find('k')
    Int_Grid_Sizes.append(int(Grid_Size[:idx]))
    print (Int_Grid_Sizes)
    list.sort(Int_Grid_Sizes)

  for Int_Grid_Size in Int_Grid_Sizes:
    for Grid_Size in Grid_Sizes:
      if (Grid_Size == '32km') and (Int_Grid_Size == 2):
        pass
      elif (Grid_Size.find(str(Int_Grid_Size)) != -1):
        Sorted_Grid_Sizes.append(Grid_Size)
  print (Sorted_Grid_Sizes)
  return (Sorted_Grid_Sizes)