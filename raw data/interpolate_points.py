from datetime import datetime, timedelta
import csv
import json

track = [
[10.5142232962, -85.3693762701],
[10.5144957919, -85.3694251366],
[10.514819501, -85.3694521263],
[10.5149628315, -85.3697231971],
[10.5152815953, -85.3701464832],
[10.5153669231, -85.3702485748],
[10.5154238362, -85.3703982756],
[10.5154310446, -85.3703097627],
[10.5153941642, -85.3702661768],
[10.5154134426, -85.370354522],
[10.5153906439, -85.370216053],
[10.5151027255, -85.3702753969],
[10.5148754083, -85.3702782467],
[10.5147875659, -85.3700907435],
[10.5143786967, -85.3702499997],
[10.5141064525, -85.370455943],
[10.5139071308, -85.3706511576],
[10.5136214755, -85.3707446158],
[10.5132000335, -85.3709037881],
[10.5129376799, -85.3711026907],
[10.512936255, -85.3712094761],
[10.5126614962, -85.3714744281],
[10.512455469, -85.3714807983],
[10.5122139025, -85.3715608455],
[10.5121593364, -85.3715491109],
[10.5122001562, -85.3714734223],
[10.5119718332, -85.371714402],
[10.5115894508, -85.3719154],
[10.5113680009, -85.3715429083],
[10.5113460403, -85.3715477698],
[10.511199357, -85.3714851569],
[10.5110747181, -85.3714516293],
[10.5108861253, -85.3713523876],
[10.5107165594, -85.3712270781],
[10.5105690379, -85.3710592724],
[10.5104124639, -85.3709099907],
[10.5103435647, -85.3708141856],
[10.5104096979, -85.3707110882],
[10.5102932733, -85.3702124488],
[10.5102663673, -85.3699607402],
[10.5101805367, -85.3696263861],
[10.5101869907, -85.3695013281],
[10.5099827237, -85.3693898488],
[10.5099088792, -85.3693779465],
[10.5097324401, -85.3693363722],
[10.5097392295, -85.3693447541],
[10.5096972361, -85.3692901041],
[10.5096553266, -85.3693072032],
[10.509641245, -85.369283231],
[10.5097161792, -85.3690960631],
[10.5094982497, -85.369107211],
[10.5094751157, -85.3686273471],
[10.5095122475, -85.368420817],
[10.5094752833, -85.3685472161],
[10.5094083119, -85.3683555219],
[10.509401774, -85.3682812583],
[10.5093779694, -85.3682250995],
[10.5092326272, -85.3682788275],
[10.5091918074, -85.3680898994],
[10.5090827588, -85.3677318245],
[10.5089663342, -85.3673937824],
[10.5089726206, -85.3673926089],
[10.5090790708, -85.3672128171],
[10.5086905695, -85.3668264113],
[10.5084061716, -85.3661556076],
[10.5084825307, -85.3662511613],
[10.5084361788, -85.3662307095],
[10.5084394477, -85.3662080783],
[10.5083796009, -85.366221657],
[10.508481944, -85.3664566018],
[10.5084490869, -85.366467163],
[10.5084374361, -85.3664661571],
[10.5084848776, -85.3664705995],
[10.5084904935, -85.3665127605],
[10.5084521882, -85.3664850164],
[10.508472221, -85.366514856],
[10.5084996298, -85.3664949909],
[10.5084993783, -85.3664185479],
[10.5085230991, -85.3664016165],
[10.5084783398, -85.3664243314],
[10.5085401144, -85.3663970903],
[10.5085039884, -85.3664929792],
[10.5086023081, -85.3666001838],
[10.5088181421, -85.3668864258],
[10.5088665895, -85.3671175148],
[10.5089958385, -85.3672770225],
[10.5089755543, -85.3672792017],
[10.5090436153, -85.3672379628],
[10.5091748759, -85.3671315126],
[10.509392973, -85.3669639584],
[10.5094271712, -85.3669109847],
[10.5096783768, -85.3669418301],
[10.5098098889, -85.3669462726],
[10.5098046921, -85.3667984996],
[10.5102035031, -85.3667916264],
[10.5102991406, -85.3668457735],
[10.5106138811, -85.3670145012],
[10.5107145477, -85.3669807222],
[10.5108235124, -85.367047023],
[10.5107096862, -85.3671737574],
[10.51158702, -85.367113743],
[10.5117197055, -85.3670808859],
[10.5118747707, -85.367180882],
[10.5121809617, -85.367062781],
[10.5121299997, -85.3670037724],
[10.5121291615, -85.3669507988],
[10.5122698098, -85.3670712467],
[10.5124614201, -85.3668787982],
[10.512432754, -85.3668642137],
[10.5128630809, -85.3666305263],
[10.513006663, -85.3664821666],
[10.5128647573, -85.3663488105],
[10.5133807473, -85.3657063376],
[10.5131341517, -85.3658920806],
[10.5131158791, -85.365895601],
[10.5131877959, -85.3658003826],
[10.5131756421, -85.3657488339],
[10.5132575333, -85.3656239435],
[10.513537908, -85.3649892658],
[10.5133240856, -85.3648470249],
[10.5135653168, -85.36488357],
[10.513939485, -85.3647746891],
[10.5141986534, -85.3645321168],
[10.514127491, -85.3643488884],
[10.5141630303, -85.3644516505],
[10.5143968016, -85.3645135928],
[10.5147999711, -85.3646423388],
[10.5147863925, -85.3644341324],
[10.5148474965, -85.3639875446],
[10.5147426389, -85.364089217],
[10.5148200877, -85.3638959303],
[10.5148163158, -85.3639779892],
[10.5150862969, -85.3634442296],
[10.5154274404, -85.3634911682],
[10.5153691862, -85.3634251188],
[10.5153800827, -85.3635928407],
[10.5152922403, -85.363434758],
[10.5153639894, -85.3633749112],
[10.5152583774, -85.3635742329],
[10.5152894743, -85.3634810261],
[10.5143646989, -85.3639992792],
[10.5143646989, -85.3639992792],
[10.5143646989, -85.3639992792],
[10.5143646989, -85.3639992792],
[10.5143646989, -85.3639992792],
[10.5143646989, -85.3639992792],
]

# time of first track time
firsttime = datetime(2014,1,24,5,36,14)

# minutes between each GPS point
intervalseconds = 5 * 60

# filename of input file with behavior data
infile = 'behavior.nocoords.csv'

outfile = 'datapoints.js'

def getinterval(time):
  index = int((time - firsttime).total_seconds() / intervalseconds)
  return track[index:index+2]


def getpoint(time):
  prev, next = getinterval(time)
  
  timediff = (time - firsttime).total_seconds()
  proportion = (timediff % intervalseconds) / float(intervalseconds)
  
  latdelta = (next[0] - prev[0])
  lat = (proportion * latdelta) + prev[0]
  
  londelta = (next[1] - prev[1])
  lon = (proportion * londelta) + prev[1]
  
  return (lat, lon)
  
  
def loadfile(filename):
  with open(filename) as csvfile:
    reader = csv.reader(csvfile)
  
    for row in reader:
      time = datetime.strptime(row[0], '%m/%d/%Y %H:%M:%S')
      yield time, row[1], row[2].strip(), int(row[3]), row[4].strip()


if __name__ == '__main__':
  points = []
  
  for row in loadfile(infile):
    lat, lon = getpoint(row[0])  
    points.append((lat, lon, row[1], row[2], row[3], row[4]))
    
  with open(outfile, 'w') as outf:
    outf.write(json.dumps(points))
    
