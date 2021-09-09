import sys
import re
import os
import glob


### estimate running time for a single n
def estimate_running_time(n):
  rt=RR(e^(log(log(n))^(2/3) * log(n)^(1/3) * (64/9)^(1/3)))
  # print "running time: \t", rt
  return rt


### compare running time for m and n
def compare_running_time(m, n):
  assert (m > n)
  rtM=estimate_running_time(m)
  rtN=estimate_running_time(n)
  print "sieving time ratio: \t", rtM/rtN
  print "matrix time ratio: \t", sqrt(rtM/rtN)


### return projected MurphyE for other_n
def return_projected_MurphyE(my_n, my_E, other_n):
  my=estimate_running_time(my_n)
  other=estimate_running_time(other_n)
  return my/other*my_E


### read folder, only looking for *.poly files
def read_polyfolder(path):

  print "<!-- Copy/Paste/Substitute from here in HTML -->"

  for filename in glob.glob(os.path.join(path, '*.poly')):
    print "<!-- comment: found", filename, "-->"

  poly_E = dict()
  poly_n = dict()
  poly_T = dict()
  poly_C = dict()
  for filename in glob.glob(os.path.join(path, '*.poly')):
    read_polyfile(poly_n, poly_E, poly_T, poly_C, filename)

  #for key, value in poly_E.iteritems():
  #print "%s: %s" % (key, value)

  index_array = [] # filename
  n_array = [] # n
  E_array = [] # Murphy E
  T_array = [] # title
  C_array = [] # comment

  # sort n
  for key, value in sorted(poly_n.iteritems(), key=lambda (k,v): (v,k)):
    index_array.append(key)
    n_array.append(value)

  size = len(poly_n)
  print "<!-- comment: Total found", size, "polynomials -->"
  # print index_array

  for i in range(size):
    T_array.append (poly_T[index_array[i]])
    E_array.append (poly_E[index_array[i]])
    C_array.append (poly_C[index_array[i]])

  ###########################
  # Row 1: print title row #
  ###########################
  print "<tr>",
  print "<th>Name</th>",
  print "<th width=\"20\">Comment</th>",
  for i in range(size):
    print "<th>" + T_array[i] + "</th>",
  print "</tr>"

  ###########################
  # Row 2: print digits row #
  ###########################
  print "<tr>",
  print "<th>Digits</th>",
  print "<td width=\"20\"></td>",
  for i in range(size):
    print "<td>" + str(ceil(RR(log(n_array[i])/log(10)))) + "</td>",
  print "</tr>"

  ########################
  # Actual rows          #
  ########################
  maxproj_E_array = [0]*size
  minproj_E_array = [1]*size

  for i in range(size):
    #print i, index_array[i], n_array[i]

    print "<tr>", # start this row

    print "<th><a href=" + index_array[i] + " target=\"_blank\" >" + T_array[i] + "</a></th>",
    print "<td width=\"20\">" + C_array[i] + "</td>",

    for j in range(size):
      expE = return_projected_MurphyE(n_array[i], E_array[i], n_array[j])

      if expE != 0:
        if expE > maxproj_E_array[j]:
          maxproj_E_array[j] = expE
        if expE < minproj_E_array[j]:
           minproj_E_array[j] = expE

      print "<td",
      if j % 2 == 0:
        print "style=\"background-color:#F0F0F0\">",
      else:
        print ">",
      if i == j:
        print "<b>" + "%.2e" % expE + "</b>",
      else:
        print "<font color=\"#4863A0\">" + "%.2e" % expE + "</font>",
      print "</td>",

    print "</tr>" # done this row

  ########################
  # Stat rows            #
  ########################
  print "<tr>",
  print "<th>Min. Proj.</th>",
  print "<td width=\"20\">min projected E for each column</td>",
  for i in range(size):
    print "<td>" + "%.2e" % minproj_E_array[i] + "</td>",
  print "</tr>"

  print "<tr>",
  print "<th>Max. Proj.</th>",
  print "<td>max projected E for each column</td>",
  for i in range(size):
    print "<td>" + "%.2e" % maxproj_E_array[i] + "</td>",
  print "</tr>"


  print "<!-- Finishing Copy/Paste/Substitute in HTML -->"

  return


### read file containing polynomials
def read_polyfile(poly_n, poly_E, poly_T, poly_C, filename):
  fi=open(filename,"r")
  s = fi.readlines()
  flag = 0
  E = 0
  name = "noname"
  comment = ""

  # s is like "# MurphyE(Bf=10000000,Bg=5000000,area=1.00e+16)=1.03e-11"
  for i in range(len(s)):

    MurphyE = re.match("# MurphyE\(Bf=(.+),Bg=(.+),area=(.+)\)=([0-9]*\.?[0-9]+e-?[0-9]+)?", s[i])
    havename = re.match("# [n|N]ame: (.+)", s[i])
    haven = re.match("^[n|N]:\s*(\d+)", s[i])
    havecomment = re.match("# [c|C]omment: (.+)", s[i])

    if haven != None:
      n = ZZ(haven.groups()[0])
      flag = 1
    if MurphyE != None:
      E = float(MurphyE.groups()[3])
    if havename != None:
      name = havename.groups()[0]
    if havecomment != None:
      comment = havecomment.groups()[0]

  if flag == 0:
    raise Exception, '# Error: must have n in', filename

  poly_n[filename] = n
  poly_E[filename] = E
  poly_T[filename] = name
  poly_C[filename] = comment

  fi.close()
  return
