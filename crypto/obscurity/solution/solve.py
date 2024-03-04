#!/usr/bin/env python3

from Crypto.Util.number import isPrime, long_to_bytes

e=65537
c=15022763214465045936744767165212746982600184065203536875227976568428939306873613476390805436083214580993019524555990698044586599588771219810740504336663277258553505356079782250716294598629534829943348568989837542600524616647776398512148768676624059936802388375310285571482677852678249660830818992599450221967914164747948899994518004258810904699907061650061554305398378203072199727875736305472447066675360230095812319156010246140601480690671346345078242002379275320945349823806278235696451119767428336324814987016517645333676211953481610383327169828525768618155157675546462005576971203760520703371346501782952380911235159521098504172414164173034564786007504921856760422189766543558765854747635588439159458818471729257537720749709199525139414681766767035764721004535814391158002132683165353735977231101364475161560392999481994653644070636582542558242077298290310358740057939463020253896560896708026058278297266702958641634293820132852079660340804616463360114181043128217820069158638587848947464620201437619460387997735666920672659538266467972568397775544232569527593694643017819173568464263347033003383687673326578304310143160515386465645036749286540220345895646229055223964851588647679073208502199905505635138830936348058395141355659919607826776930166890844720804635091238630540159622465355317689435529072169630164982836533057604805600931031795961446370104177535650256072979585823033389636727204550883489043219021732931951049135369167148313268841110823945087570257086408122199615570811762087720098847734699897948571161397568586601916732814087731450570920942328622925605409596220590745367037909511647679088498094798808490759098844688066131034855970925651099080581146914793696775426335659188919210813627849923020851250273138556370677582899644439625092011586084999870907143909116541893516957807492477712900424543497712077270520762635823197094364729529694114480018279369229055201082162923387973620966437754011413563079119592217303640920273788925915302708715315859820701431521360211984187323835490610118622994902741285280925005774973905070883034410828730572711116062338735159270955271740847905049317067398797300236434323795955904041481401126071862461056676367975079316744362673484493674289555710966368636020310439053786583600555298714831293080559598860687707324824123396309856789300675081496896375714606233610707084501540738610962550925419653316060901872939928301385848818695441798692668162311439777249483552553715904260792716187943232294424269259756622758890647884330367240346492821355459252127824673556547078620065038629381350781206887169675838222873781273904633952061710221848717778220698010084685018281813200978752582423573471963497669849562477758983099171678960375524443161562709433341745175732145775464901129204410679843472777747901752165083835626067873887252025344976684724038473273853258054979998035423713252950925326278533094371049607219431503714837501124624028358036248508942102870551638364486378605948059980645413319965490800475173369757494631738535182095729956573803370857948282056319393380084100929677135381914837593599685768704411034606031441064673038698198021437204090766558580302831501088819461770195970278140239116523934036685977461101130191845179362549430121119597963651238498968175925698485151113008947344713159356141492443625034625585318003876146779329926289650450302014597856969312657439406752529136161186513106071393879699017976166707858070997296279000185035485662828915514580407570559730127956659983734340894341215044365351727533491746994651883197805007139287169022202161291991090278014046750623606408919844930698216109415189197150148530276107218945840855996277311740411568300229862782731159365533295739107914847134713104864430480997649399023973400045386949283900587874025689742469755113887898409368133594920178808656560838838938141272973388515897745868203894865217266350754764015324421585429401694052850619882630367163453104501831851317008304810591814765054122378551356036403553158912853586939642811011193573688831164125173135218399203542193496031810187087979245883096946868486231352946485719488838433370860164117457307845391737283972906791910664482475633112288347908145271605474025641091182749650043999390459959319174423664862048867247709866351952685798933061673491275941458168391899719077896883099136500531476965313670170150941893243633635703599053162315030844693532622987104293
n=59490679579998635868564022242503445659680322440679327938309703916140405638383434744833220555452130558140772894046169700747186409941317550665821619479140098743288335106272856533978719769677794737287419461899922456614256826709727133515885581878614846298251428096512495590545989536239739285290509870860732435109794045491640561011775744617218426011793283330497878491137999673760740717904979730106994180691956740996319139767941335979146924614249205862051182094081815447356600355657858936442589201739350474320966093143098768914226528498860747050474426418211313776073365498029087492308102876323562641651940555529817223923967479711293692697592800750806084802623966596666156361791014935954720420383555300213829134029560826306201326905674141090667002959274513478562033467485802590354539887133866434256562999666615074220857502563011098759348850149774083443643246907501430076141377431759984926248272553982527014011245310690986644461251576837779050124866641531488351016070300247918750613207952783437248236577750579092103591540592540838395240861443615842939673889972504776455114767522430347610500271801944701491874649306605557851914677316523034726044356368337787113190245601235705959816327016988315321850324065292964680148884818699916224411245926491625245571963741062587277736372090007125908660590314049976206281064703285728879581199596401313352724403492043120507597057004633720111008838673185885941472392623805512709896864520875740497617898566981218781313900004406341154884180472153171064617953661517880143988867189622824081729539392205701820144922307223627345876707465251206005262622236311161449785941834002795854996108322186230425179217618301526151712928790928933798369678844576216735378555233905935973195721247604933753363412045618703247367192610615234835041956551569232557323060407648325565048712478527583315981204846341857095134567470182330491262285172727037299211391244340592936174221176781260586188162350081192408213470101717320475998863222409777310443027421196981193126541663212124245716187453863438039402316877152286468198891603632606578778749292403571792687832081974134637014026451921536576338243322267400651083805535119025415817887075652758045539565968044552126338330231434466204888993650859153585380124240540573308417330478048240203241631072371322849430883727355239704116556046700749530006852187064160849175332758172150251213637470549781080491037088372092203085237973008861896576796238915011886636658033019385943299986285181723378096425117379056207797455963451889971988904466449319007760192467211209692128894691704353648198130409333996534250878389064152054828983825841234644875996912485916827004219887033833599723481903489316488764021700996686817244736947119285629049355809027206179193628292018441744552168286541735687924729198455883895791600170372255284216915442808139396541702893732917062958054499525549626455191658842064247047426187897146172971001949767308335268505414284088528125611263685734457560292833389995980698745893243832547007166243476192958601735336260255598581701267151224204461879782815468518040925292817115377696676461775120750971210951527384637825092221708015393564320979357698186262039029460777050248162599194429941464248920952161182024344007059684970270762248243899640259750891406957836740989312390963091260380990901672119736141666856448171380781556117025832312710039041398538035351795267732240730608951176127282191528457681241590895740457571038936173983449289126574141189374690274057472401359482497502067814596008557725079835212621242944853319496441084441343866446380876967613370281793088540430288658573281302876742323336651987699532240686371751448290351615451932054274752105688318766958111191822471878078268490672607804265064578569581247796205593441336042254502454646980009177290888726099355974892680373341371214123450598691915802122913613669446370194221846225597401405625536693874723700374068542217340621938985167525416725638580266200550048001242788847319217369432802469735271132107428204697172144851088692772696511622350096452418244968500432645305761138012204888798724453956720733374364721511323104353496583927094760495687785031050687852300161433757934364774351673531859394855389527851678630166084819717354779333605871648837631164630550613112327670353108353791304451834904017538583880634608113426156225757314283269948216017294095002859515842577481167417167637534527111130468710


phi = 1
e = 65537
for i in range(10000):
    if isPrime(i):
        phi *= i-1



d = pow(e, -1, phi)

f = pow(c, d, n)


print(long_to_bytes(f))