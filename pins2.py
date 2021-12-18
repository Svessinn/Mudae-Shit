def main():
	lst = []
	lsst = []
	for i in range(1, 722):
		lsst.append('pin'+str(i))
	for i in range(1, 93):
		lsst.append('logopin'+str(i))
	inp = input('$mpda other\n')
	while inp:
		ls = inp.split(' ​ ')
		for i in ls:
			if i != '':
				if int(i.split('x')[-1].strip().encode('ascii', 'ignore')) > 5:
					lst.append(i.split(':')[1])
					lsst.remove(i.split(':')[1])
		inp = input()
	inp = input('$mpa you\n')
	while inp:
		ls = inp[1:-1].split('::')
		for i in ls:
			if i in lst:
				lst.remove(i)
		inp = input()
	out = lst
	lst = []
	inp = input('$mpda you\n')
	while inp:
		ls = inp.split(' ​ ')
		for i in ls:
			if i != '':
				if i.split(':')[1] in lsst:
					lst.append(i.split(':')[1])
		inp = input()
	print(*out, sep='$')
	print(*lst, sep='$')













	pins = '''
:pin1:x2 ​ :pin2:x4 ​ :pin3:x6 ​ :pin4:x2 ​ :pin5:x2 ​ :pin6:x5 ​ :pin7:x3 ​ :pin8:x4 ​ :pin9:x2 ​ 
:pin10:x4 ​ :pin11:x8 ​ :pin12:x3 ​ :pin13:x2 ​ :pin14:x2 ​ :pin15:x6 ​ :pin16:x8 ​ :pin17:x4 ​ :pin18:x5 ​ 
:pin19:x2 ​ :pin20:x7 ​ :pin21:x2 ​ :pin22:x3 ​ :pin23:x3 ​ :pin24:x3 ​ :pin25:x8 ​ :pin26:x2 ​ :pin27:x7 ​
:pin28:x6 ​ :pin29:x2 ​ :pin31:x2 ​ :pin32:x2 ​ :pin33:x6 ​ :pin34:x5 ​ :pin35:x6 ​ :pin36:x7 ​ :pin37:x4 ​ 
:pin39:x2 ​ :pin40:x2 ​ :pin41:x6 ​ :pin42:x3 ​ :pin43:x5 ​ :pin44:x4 ​ :pin45:x6 ​ :pin46:x6 ​ :pin47:x4 ​ 
:pin48:x4 ​ :pin49:x5 ​ :pin50:x6 ​ :pin51:x2 ​ :pin53:x2 ​ :pin54:x4 ​ :pin55:x5 ​ :pin56:x5 ​ :pin57:x3 ​
:pin58:x2 ​ :pin59:x7 ​ :pin60:x2 ​ :pin61:x5 ​ :pin62:x3 ​ :pin63:x3 ​ :pin64:x6 ​ :pin65:x7 ​ :pin66:x4 ​ 
:pin67:x3 ​ :pin68:x2 ​ :pin69:x4 ​ :pin70:x2 ​ :pin71:x5 ​ :pin72:x2 ​ :pin73:x3 ​ :pin74:x5 ​ :pin75:x3 ​ 
:pin76:x6 ​ :pin77:x4 ​ :pin78:x6 ​ :pin79:x7 ​ :pin80:x4 ​ :pin81:x3 ​ :pin82:x2 ​ :pin83:x4 ​ :pin84:x4 ​
:pin85:x4 ​ :pin86:x5 ​ :pin87:x3 ​ :pin88:x3 ​ :pin89:x3 ​ :pin90:x4 ​ :pin91:x3 ​ :pin92:x2 ​ :pin93:x4 ​ 
:pin94:x6 ​ :pin95:x5 ​ :pin96:x6 ​ :pin97:x4 ​ :pin98:x2 ​ :pin99:x2 ​ :pin100:x4 ​ :pin101:x2 ​ :pin102:x2 ​ 
:pin103:x4 ​ :pin104:x4 ​ :pin105:x5 ​ :pin106:x4 ​ :pin107:x2 ​ :pin108:x5 ​ :pin109:x3 ​ :pin110:x3 ​ :pin111:x4 ​
:pin112:x6 ​ :pin113:x7 ​ :pin114:x2 ​ :pin115:x4 ​ :pin116:x6 ​ :pin117:x7 ​ :pin118:x5 ​ :pin119:x8 ​ :pin120:x4 ​ 
:pin121:x3 ​ :pin122:x4 ​ :pin123:x5 ​ :pin124:x4 ​ :pin125:x4 ​ :pin126:x3 ​ :pin127:x3 ​ :pin128:x2 ​ :pin129:x3 ​ 
:pin130:x6 ​ :pin131:x7 ​ :pin132:x7 ​ :pin134:x6 ​ :pin135:x5 ​ :pin136:x4 ​ :pin137:x4 ​ :pin138:x6 ​ :pin140:x5 ​
:pin141:x3 ​ :pin142:x2 ​ :pin143:x3 ​ :pin144:x3 ​ :pin145:x3 ​ :pin146:x2 ​ :pin147:x4 ​ :pin148:x7 ​ :pin149:x5 ​ 
:pin150:x5 ​ :pin151:x2 ​ :pin152:x6 ​ :pin153:x3 ​ :pin154:x6 ​ :pin155:x5 ​ :pin156:x4 ​ :pin157:x3 ​ :pin158:x6 ​ 
:pin159:x6 ​ :pin160:x3 ​ :pin161:x2 ​ :pin162:x4 ​ :pin164:x4 ​ :pin165:x3 ​ :pin166:x3 ​ :pin167:x4 ​ :pin168:x8 ​
:pin169:x3 ​ :pin170:x5 ​ :pin171:x3 ​ :pin172:x5 ​ :pin173:x3 ​ :pin174:x6 ​ :pin175:x4 ​ :pin176:x8 ​ :pin177:x5 ​ 
:pin178:x6 ​ :pin179:x4 ​ :pin181:x3 ​ :pin182:x3 ​ :pin184:x4 ​ :pin185:x4 ​ :pin186:x7 ​ :pin187:x7 ​ :pin188:x2 ​ 
:pin189:x2 ​ :pin190:x4 ​ :pin191:x4 ​ :pin192:x5 ​ :pin193:x2 ​ :pin194:x4 ​ :pin195:x4 ​ :pin196:x4 ​ :pin197:x7 ​
:pin198:x6 ​ :pin199:x3 ​ :pin200:x4 ​ :pin202:x8 ​ :pin203:x5 ​ :pin204:x3 ​ :pin205:x3 ​ :pin206:x6 ​ :pin207:x6 ​ 
:pin208:x2 ​ :pin209:x3 ​ :pin210:x6 ​ :pin211:x3 ​ :pin212:x5 ​ :pin213:x2 ​ :pin215:x3 ​ :pin216:x4 ​ :pin217:x9 ​ 
:pin218:x7 ​ :pin219:x5 ​ :pin220:x6 ​ :pin221:x9 ​ :pin222:x10 ​ :pin223:x4 ​ :pin224:x3 ​ :pin225:x8 ​ :pin226:x6 ​
:pin228:x3 ​ :pin229:x5 ​ :pin230:x5 ​ :pin231:x5 ​ :pin232:x4 ​ :pin233:x7 ​ :pin234:x6 ​ :pin235:x9 ​ :pin236:x2 ​ 
:pin237:x4 ​ :pin238:x4 ​ :pin239:x2 ​ :pin240:x4 ​ :pin241:x6 ​ :pin242:x3 ​ :pin243:x4 ​ :pin244:x4 ​ :pin245:x5 ​ 
:pin246:x5 ​ :pin247:x2 ​ :pin248:x3 ​ :pin249:x6 ​ :pin250:x4 ​ :pin251:x2 ​ :pin252:x3 ​ :pin253:x3 ​ :pin254:x6 ​
:pin255:x3 ​ :pin256:x2 ​ :pin257:x2 ​ :pin258:x3 ​ :pin259:x4 ​ :pin260:x3 ​ :pin261:x6 ​ :pin262:x8 ​ :pin263:x5 ​ 
:pin264:x4 ​ :pin265:x4 ​ :pin266:x7 ​ :pin267:x4 ​ :pin268:x5 ​ :pin270:x4 ​ :pin271:x2 ​ :pin272:x9 ​ :pin273:x6 ​ 
:pin274:x2 ​ :pin275:x2 ​ :pin277:x7 ​ :pin278:x4 ​ :pin279:x4 ​ :pin281:x5 ​ :pin282:x6 ​ :pin283:x3 ​ :pin284:x2 ​
:pin285:x3 ​ :pin286:x4 ​ :pin287:x4 ​ :pin288:x9 ​ :pin289:x9 ​ :pin290:x6 ​ :pin291:x4 ​ :pin292:x3 ​ :pin293:x6 ​ 
:pin294:x3 ​ :pin295:x6 ​ :pin296:x2 ​ :pin297:x6 ​ :pin298:x5 ​ :pin299:x6 ​ :pin300:x4 ​ :pin301:x6 ​ :pin302:x5 ​ 
:pin303:x5 ​ :pin304:x6 ​ :pin305:x5 ​ :pin306:x4 ​ :pin307:x6 ​ :pin308:x2 ​ :pin309:x9 ​ :pin310:x5 ​ :pin311:x5 ​
:pin312:x7 ​ :pin314:x4 ​ :pin315:x4 ​ :pin316:x4 ​ :pin317:x3 ​ :pin319:x5 ​ :pin320:x8 ​ :pin321:x6 ​ :pin322:x8 ​ 
:pin323:x3 ​ :pin324:x6 ​ :pin325:x4 ​ :pin326:x3 ​ :pin327:x3 ​ :pin328:x4 ​ :pin329:x4 ​ :pin330:x3 ​ :pin331:x5 ​ 
:pin332:x4 ​ :pin333:x3 ​ :pin334:x2 ​ :pin335:x6 ​ :pin336:x4 ​ :pin337:x5 ​ :pin338:x4 ​ :pin339:x2 ​ :pin340:x3 ​
:pin341:x5 ​ :pin342:x8 ​ :pin343:x4 ​ :pin344:x4 ​ :pin345:x9 ​ :pin346:x6 ​ :pin347:x2 ​ :pin348:x5 ​ :pin349:x2 ​ 
:pin350:x7 ​ :pin351:x2 ​ :pin352:x4 ​ :pin353:x3 ​ :pin354:x5 ​ :pin355:x2 ​ :pin356:x4 ​ :pin357:x5 ​ :pin358:x6 ​ 
:pin359:x4 ​ :pin360:x6 ​ :pin361:x4 ​ :pin362:x6 ​ :pin363:x2 ​ :pin364:x5 ​ :pin365:x8 ​ :pin368:x4 ​ :pin369:x6 ​
:pin370:x4 ​ :pin371:x4 ​ :pin372:x3 ​ :pin373:x3 ​ :pin374:x3 ​ :pin375:x3 ​ :pin376:x4 ​ :pin377:x6 ​ :pin378:x5 ​ 
:pin379:x6 ​ :pin380:x5 ​ :pin381:x4 ​ :pin382:x2 ​ :pin383:x6 ​ :pin384:x2 ​ :pin386:x5 ​ :pin387:x3 ​ :pin388:x4 ​ 
:pin389:x8 ​ :pin390:x4 ​ :pin391:x4 ​ :pin392:x4 ​ :pin393:x3 ​ :pin394:x5 ​ :pin395:x3 ​ :pin396:x4 ​ :pin397:x5 ​
:pin398:x6 ​ :pin399:x8 ​ :pin400:x3 ​ :pin401:x4 ​ :pin402:x6 ​ :pin403:x3 ​ :pin404:x5 ​ :pin405:x2 ​ :pin406:x2 ​ 
:pin407:x3 ​ :pin408:x4 ​ :pin409:x7 ​ :pin410:x7 ​ :pin411:x5 ​ :pin412:x4 ​ :pin413:x3 ​ :pin414:x8 ​ :pin415:x5 ​ 
:pin418:x5 ​ :pin419:x5 ​ :pin420:x5 ​ :pin421:x3 ​ :pin423:x6 ​ :pin424:x4 ​ :pin425:x2 ​ :pin426:x7 ​ :pin427:x5 ​
:pin428:x3 ​ :pin429:x9 ​ :pin430:x3 ​ :pin431:x2 ​ :pin432:x5 ​ :pin433:x2 ​ :pin434:x4 ​ :pin435:x2 ​ :pin436:x4 ​ 
:pin437:x6 ​ :pin438:x6 ​ :pin439:x4 ​ :pin440:x2 ​ :pin441:x2 ​ :pin442:x3 ​ :pin443:x5 ​ :pin445:x6 ​ :pin446:x5 ​ 
:pin447:x3 ​ :pin448:x3 ​ :pin449:x5 ​ :pin450:x2 ​ :pin451:x4 ​ :pin452:x7 ​ :pin453:x5 ​ :pin455:x3 ​ :pin456:x5 ​
:pin457:x4 ​ :pin459:x6 ​ :pin460:x5 ​ :pin461:x3 ​ :pin462:x3 ​ :pin463:x3 ​ :pin464:x3 ​ :pin465:x2 ​ :pin466:x2 ​ 
:pin467:x3 ​ :pin468:x3 ​ :pin469:x6 ​ :pin470:x6 ​ :pin471:x4 ​ :pin472:x3 ​ :pin474:x5 ​ :pin476:x6 ​ :pin477:x6 ​ 
:pin478:x5 ​ :pin479:x4 ​ :pin480:x3 ​ :pin481:x5 ​ :pin482:x3 ​ :pin483:x4 ​ :pin484:x2 ​ :pin485:x3 ​ :pin486:x4 ​
:pin487:x4 ​ :pin488:x4 ​ :pin489:x5 ​ :pin490:x3 ​ :pin491:x5 ​ :pin492:x4 ​ :pin493:x3 ​ :pin494:x2 ​ :pin495:x6 ​ 
:pin496:x4 ​ :pin497:x2 ​ :pin498:x3 ​ :pin499:x2 ​ :pin500:x4 ​ :pin501:x5 ​ :pin502:x4 ​ :pin503:x2 ​ :pin504:x3 ​ 
:pin505:x4 ​ :pin506:x6 ​ :pin507:x4 ​ :pin508:x6 ​ :pin509:x5 ​ :pin510:x8 ​ :pin511:x2 ​ :pin512:x7 ​ :pin513:x4 ​
:pin514:x5 ​ :pin515:x3 ​ :pin516:x3 ​ :pin517:x2 ​ :pin518:x5 ​ :pin519:x3 ​ :pin520:x4 ​ :pin521:x4 ​ :pin523:x5 ​ 
:pin524:x5 ​ :pin525:x2 ​ :pin526:x7 ​ :pin527:x3 ​ :pin528:x3 ​ :pin530:x7 ​ :pin531:x5 ​ :pin532:x3 ​ :pin533:x5 ​ 
:pin534:x5 ​ :pin535:x6 ​ :pin536:x5 ​ :pin537:x2 ​ :pin538:x5 ​ :pin539:x5 ​ :pin541:x6 ​ :pin542:x4 ​ :pin543:x4 ​
:pin544:x5 ​ :pin545:x6 ​ :pin546:x3 ​ :pin547:x3 ​ :pin548:x3 ​ :pin549:x3 ​ :pin550:x4 ​ :pin551:x3 ​ :pin552:x3 ​ 
:pin553:x3 ​ :pin554:x4 ​ :pin555:x4 ​ :pin556:x4 ​ :pin557:x5 ​ :pin558:x7 ​ :pin559:x5 ​ :pin560:x5 ​ :pin561:x2 ​ 
:pin562:x10 ​ :pin564:x7 ​ :pin565:x2 ​ :pin566:x6 ​ :pin567:x3 ​ :pin568:x6 ​ :pin569:x6 ​ :pin572:x5 ​ :pin573:x8 ​
:pin575:x8 ​ :pin576:x2 ​ :pin577:x12 ​ :pin578:x5 ​ :pin579:x7 ​ :pin580:x6 ​ :pin581:x3 ​ :pin582:x7 ​ :pin583:x8 ​ 
:pin584:x4 ​ :pin585:x7 ​ :pin586:x4 ​ :pin587:x7 ​ :pin588:x3 ​ :pin589:x6 ​ :pin590:x7 ​ :pin591:x3 ​ :pin592:x5 ​ 
:pin593:x4 ​ :pin594:x3 ​ :pin595:x5 ​ :pin596:x3 ​ :pin597:x3 ​ :pin598:x3 ​ :pin600:x2 ​ :pin601:x2 ​ :pin602:x4 ​
:pin603:x7 ​ :pin604:x5 ​ :pin605:x6 ​ :pin606:x3 ​ :pin607:x7 ​ :pin608:x4 ​ :pin609:x4 ​ :pin610:x6 ​ :pin612:x2 ​ 
:pin613:x3 ​ :pin614:x3 ​ :pin615:x4 ​ :pin617:x3 ​ :pin618:x7 ​ :pin619:x6 ​ :pin620:x6 ​ :pin621:x5 ​ :pin622:x3 ​ 
:pin623:x4 ​ :pin624:x6 ​ :pin625:x6 ​ :pin626:x4 ​ :pin627:x6 ​ :pin628:x3 ​ :pin629:x2 ​ :pin630:x4 ​ :pin631:x3 ​
:pin632:x4 ​ :pin633:x3 ​ :pin634:x9 ​ :pin635:x3 ​ :pin636:x2 ​ :pin637:x3 ​ :pin638:x4 ​ :pin639:x5 ​ :pin640:x6 ​ 
:pin641:x4 ​ :pin642:x3 ​ :pin643:x3 ​ :pin644:x4 ​ :pin645:x6 ​ :pin646:x3 ​ :pin647:x5 ​ :pin648:x3 ​ :pin649:x4 ​ 
:pin650:x7 ​ :pin651:x2 ​ :pin652:x8 ​ :pin653:x2 ​ :pin654:x5 ​ :pin655:x3 ​ :pin656:x5 ​ :pin658:x6 ​ :pin659:x5 ​
:pin660:x2 ​ :pin661:x5 ​ :pin662:x6 ​ :pin663:x6 ​ :pin664:x4 ​ :pin665:x2 ​ :pin666:x7 ​ :pin668:x4 ​ :pin669:x6 ​ 
:pin670:x2 ​ :pin671:x3 ​ :pin673:x4 ​ :pin674:x3 ​ :pin675:x5 ​ :pin676:x3 ​ :pin677:x2 ​ :pin678:x6 ​ :pin679:x3 ​ 
:pin680:x4 ​ :pin681:x2 ​ :pin683:x6 ​ :pin684:x6 ​ :pin685:x4 ​ :pin686:x4 ​ :pin687:x3 ​ :pin688:x2 ​ :pin689:x8 ​
:pin690:x5 ​ :pin691:x2 ​ :pin692:x3 ​ :pin693:x4 ​ :pin694:x4 ​ :pin695:x5 ​ :pin696:x4 ​ :pin697:x4 ​ :pin698:x3 ​ 
:pin699:x4 ​ :pin700:x2 ​ :pin701:x3 ​ :pin702:x3 ​ :pin703:x7 ​ :pin704:x5 ​ :pin705:x4 ​ :pin706:x2 ​ :pin707:x5 ​ 
:pin708:x6 ​ :pin709:x3 ​ :pin710:x3 ​ :pin711:x5 ​ :pin712:x5 ​ :pin713:x6 ​ :pin714:x5 ​ :pin715:x5 ​ :pin716:x5 ​
:pin717:x6 ​ :pin718:x5 ​ :pin719:x3 ​ :pin720:x4 ​ :pin721:x2 ​ :logopin1:x3 ​ :logopin2:x4 ​ :logopin3:x3 ​ :logopin4:x4 ​ 
:logopin6:x5 ​ :logopin7:x4 ​ :logopin8:x9 ​ :logopin9:x4 ​ :logopin10:x3 ​ :logopin11:x3 ​ :logopin12:x4 ​ :logopin13:x5 ​ :logopin14:x4 ​ 
:logopin15:x3 ​ :logopin16:x7 ​ :logopin17:x6 ​ :logopin18:x3 ​ :logopin19:x5 ​ :logopin20:x6 ​ :logopin21:x2 ​ :logopin23:x7 ​ :logopin24:x5 ​
:logopin26:x4 ​ :logopin27:x5 ​ :logopin28:x4 ​ :logopin29:x5 ​ :logopin30:x4 ​ :logopin31:x6 ​ :logopin32:x4 ​ :logopin33:x9 ​ :logopin34:x3 ​ 
:logopin35:x8 ​ :logopin36:x3 ​ :logopin37:x4 ​ :logopin38:x3 ​ :logopin39:x3 ​ :logopin40:x7 ​ :logopin41:x6 ​ :logopin42:x5 ​ :logopin43:x6 ​ 
:logopin44:x3 ​ :logopin45:x5 ​ :logopin46:x5 ​ :logopin47:x4 ​ :logopin48:x9 ​ :logopin49:x7 ​ :logopin51:x4 ​ :logopin52:x4 ​ :logopin54:x6 ​
:logopin55:x7 ​ :logopin57:x6 ​ :logopin58:x4 ​ :logopin59:x9 ​ :logopin60:x3 ​ :logopin61:x5 ​ :logopin62:x4 ​ :logopin63:x3 ​ :logopin64:x3 ​ 
:logopin65:x4 ​ :logopin66:x2 ​ :logopin67:x4 ​ :logopin68:x3 ​ :logopin69:x5 ​ :logopin70:x5 ​ :logopin71:x3 ​ :logopin72:x3 ​ :logopin73:x6 ​ 
:logopin74:x6 ​ :logopin75:x6 ​ :logopin76:x6 ​ :logopin77:x4 ​ :logopin78:x8 ​ :logopin79:x5 ​ :logopin80:x2 ​ :logopin81:x10 ​ :logopin82:x11 ​
:logopin83:x3 ​ :logopin84:x4 ​ :logopin85:x3 ​ :logopin87:x3 ​ :logopin88:x8 ​ :logopin89:x5 ​ :logopin90:x3 ​ :logopin91:x4 ​ :logopin92:x3 ​

:pin1::pin3::pin4::pin5::pin6::pin7::pin8::pin9::pin10:
:pin11::pin12::pin13::pin14::pin15::pin16::pin17::pin18::pin20:
:pin21::pin22::pin24::pin25::pin26::pin27::pin28::pin29::pin30:
:pin31::pin32::pin33::pin36::pin37::pin39::pin40::pin41::pin42:
:pin43::pin44::pin45::pin46::pin47::pin48::pin49::pin50::pin51:
:pin52::pin53::pin54::pin55::pin56::pin57::pin58::pin59::pin60:
:pin61::pin62::pin63::pin64::pin65::pin66::pin67::pin69::pin70:
:pin71::pin72::pin74::pin75::pin76::pin77::pin78::pin79::pin80:
:pin81::pin82::pin84::pin85::pin86::pin87::pin88::pin89::pin90:
:pin91::pin92::pin93::pin94::pin95::pin96::pin97::pin98::pin99:
:pin100::pin101::pin102::pin103::pin104::pin105::pin106::pin107::pin108:
:pin109::pin110::pin111::pin112::pin114::pin115::pin116::pin117::pin118:
:pin119::pin120::pin121::pin122::pin123::pin124::pin125::pin126::pin127:
:pin129::pin130::pin131::pin133::pin134::pin135::pin136::pin137::pin138:
:pin139::pin140::pin141::pin142::pin143::pin144::pin145::pin146::pin148:
:pin149::pin150::pin151::pin152::pin154::pin155::pin156::pin157::pin158:
:pin159::pin160::pin161::pin162::pin163::pin164::pin165::pin166::pin167:
:pin168::pin169::pin170::pin172::pin174::pin176::pin177::pin178::pin179:
:pin180::pin181::pin182::pin183::pin184::pin185::pin186::pin187::pin190:
:pin191::pin192::pin193::pin194::pin195::pin196::pin197::pin198::pin199:
:pin200::pin201::pin202::pin203::pin204::pin205::pin206::pin207::pin208:
:pin209::pin210::pin212::pin213::pin214::pin215::pin216::pin218::pin219:
:pin220::pin221::pin222::pin223::pin224::pin227::pin228::pin229::pin230:
:pin231::pin233::pin234::pin236::pin238::pin239::pin240::pin241::pin242:
:pin243::pin244::pin246::pin247::pin248::pin249::pin250::pin253::pin254:
:pin255::pin256::pin257::pin258::pin259::pin260::pin261::pin263::pin265:
:pin266::pin268::pin269::pin270::pin271::pin272::pin273::pin275::pin276:
:pin277::pin278::pin279::pin280::pin281::pin282::pin283::pin284::pin285:
:pin286::pin287::pin288::pin290::pin291::pin292::pin293::pin294::pin296:
:pin297::pin298::pin299::pin300::pin301::pin302::pin303::pin304::pin306:
:pin307::pin309::pin310::pin311::pin312::pin313::pin315::pin316::pin317:
:pin318::pin319::pin320::pin321::pin322::pin323::pin325::pin326::pin327:
:pin328::pin329::pin330::pin331::pin332::pin333::pin334::pin335::pin336:
:pin337::pin338::pin339::pin340::pin343::pin344::pin346::pin347::pin348:
:pin349::pin350::pin351::pin352::pin353::pin355::pin357::pin359::pin361:
:pin362::pin363::pin364::pin366::pin367::pin368::pin369::pin370::pin371:
:pin372::pin373::pin374::pin375::pin376::pin377::pin378::pin379::pin380:
:pin381::pin382::pin384::pin385::pin386::pin387::pin388::pin389::pin390:
:pin391::pin392::pin393::pin394::pin395::pin397::pin398::pin399::pin400:
:pin401::pin402::pin403::pin404::pin405::pin406::pin407::pin408::pin409:
:pin410::pin411::pin412::pin413::pin414::pin415::pin416::pin421::pin422:
:pin423::pin424::pin425::pin426::pin427::pin428::pin429::pin430::pin431:
:pin432::pin433::pin434::pin435::pin436::pin437::pin438::pin439::pin440:
:pin441::pin442::pin443::pin444::pin445::pin447::pin448::pin449::pin450:
:pin451::pin452::pin453::pin455::pin456::pin457::pin458::pin459::pin460:
:pin461::pin462::pin463::pin464::pin465::pin466::pin467::pin468::pin469:
:pin470::pin471::pin472::pin473::pin474::pin475::pin476::pin477::pin478:
:pin479::pin480::pin482::pin483::pin484::pin485::pin486::pin487::pin488:
:pin489::pin490::pin491::pin492::pin493::pin494::pin495::pin496::pin497:
:pin498::pin499::pin501::pin502::pin503::pin504::pin505::pin506::pin507:
:pin508::pin509::pin510::pin511::pin512::pin514::pin515::pin516::pin517:
:pin518::pin519::pin520::pin521::pin522::pin523::pin524::pin525::pin526:
:pin527::pin530::pin531::pin532::pin533::pin534::pin535::pin536::pin537:
:pin538::pin539::pin541::pin542::pin543::pin544::pin545::pin547::pin548:
:pin549::pin551::pin552::pin553::pin555::pin556::pin557::pin558::pin559:
:pin560::pin561::pin562::pin563::pin564::pin565::pin566::pin567::pin568:
:pin569::pin570::pin571::pin572::pin573::pin574::pin575::pin576::pin577:
:pin578::pin579::pin580::pin581::pin582::pin583::pin584::pin585::pin586:
:pin587::pin588::pin589::pin590::pin591::pin592::pin593::pin594::pin595:
:pin597::pin598::pin599::pin600::pin601::pin602::pin603::pin604::pin605:
:pin606::pin607::pin608::pin610::pin611::pin613::pin614::pin615::pin616:
:pin617::pin618::pin619::pin620::pin621::pin622::pin623::pin624::pin625:
:pin626::pin627::pin629::pin630::pin631::pin632::pin633::pin634::pin635:
:pin636::pin638::pin639::pin641::pin643::pin644::pin645::pin646::pin647:
:pin648::pin649::pin650::pin651::pin652::pin653::pin654::pin655::pin656:
:pin657::pin658::pin659::pin660::pin662::pin663::pin664::pin665::pin666:
:pin667::pin668::pin669::pin670::pin671::pin672::pin673::pin674::pin675:
:pin676::pin677::pin678::pin679::pin680::pin681::pin683::pin685::pin686:
:pin687::pin688::pin689::pin690::pin692::pin693::pin694::pin695::pin696:
:pin697::pin698::pin699::pin700::pin701::pin702::pin703::pin704::pin705:
:pin706::pin707::pin708::pin709::pin710::pin711::pin712::pin713::pin714:
:pin715::pin716::pin718::pin719::pin720::pin721::logopin1::logopin2::logopin4:
:logopin5::logopin6::logopin7::logopin9::logopin10::logopin11::logopin12::logopin13::logopin14:
:logopin15::logopin16::logopin18::logopin19::logopin20::logopin21::logopin22::logopin23::logopin24:
:logopin25::logopin26::logopin30::logopin31::logopin32::logopin33::logopin34::logopin35::logopin36:
:logopin37::logopin38::logopin39::logopin40::logopin41::logopin42::logopin43::logopin44::logopin45:
:logopin46::logopin47::logopin48::logopin49::logopin50::logopin51::logopin52::logopin53::logopin54:
:logopin55::logopin56::logopin57::logopin58::logopin59::logopin60::logopin61::logopin62::logopin65:
:logopin66::logopin67::logopin68::logopin70::logopin71::logopin72::logopin73::logopin74::logopin75:
:logopin76::logopin77::logopin78::logopin80::logopin81::logopin82::logopin83::logopin84::logopin86:
:logopin87::logopin88::logopin89::logopin90::logopin91::logopin92:

:pin7:x2 ​ :pin14:x2 ​ :pin26:x2 ​ :pin28:x2 ​ :pin55:x2 ​ :pin56:x2 ​ :pin71:x2 ​ :pin135:x2 ​ :pin143:x2 ​ 
:pin146:x2 ​ :pin156:x2 ​ :pin159:x2 ​ :pin162:x2 ​ :pin172:x2 ​ :pin177:x2 ​ :pin180:x2 ​ :pin181:x2 ​ :pin186:x2 ​ 
:pin198:x4 ​ :pin200:x2 ​ :pin205:x3 ​ :pin206:x2 ​ :pin222:x2 ​ :pin236:x2 ​ :pin257:x3 ​ :pin269:x2 ​ :pin273:x2 ​
:pin276:x3 ​ :pin278:x2 ​ :pin280:x3 ​ :pin281:x2 ​ :pin282:x2 ​ :pin294:x2 ​ :pin297:x2 ​ :pin303:x3 ​ :pin309:x2 ​ 
:pin319:x3 ​ :pin329:x2 ​ :pin333:x2 ​ :pin343:x3 ​ :pin348:x2 ​ :pin350:x2 ​ :pin355:x2 ​ :pin357:x2 ​ :pin369:x2 ​ 
:pin375:x2 ​ :pin378:x5 ​ :pin386:x2 ​ :pin390:x2 ​ :pin399:x3 ​ :pin412:x2 ​ :pin415:x3 ​ :pin427:x2 ​ :pin435:x4 ​
:pin447:x2 ​ :pin448:x3 ​ :pin449:x3 ​ :pin453:x2 ​ :pin464:x2 ​ :pin468:x2 ​ :pin472:x2 ​ :pin478:x2 ​ :pin479:x3 ​ 
:pin483:x2 ​ :pin488:x3 ​ :pin504:x2 ​ :pin510:x2 ​ :pin511:x2 ​ :pin522:x2 ​ :pin527:x2 ​ :pin531:x5 ​ :pin543:x2 ​ 
:pin544:x2 ​ :pin551:x3 ​ :pin552:x2 ​ :pin555:x2 ​ :pin569:x3 ​ :pin579:x3 ​ :pin581:x3 ​ :pin586:x2 ​ :pin587:x4 ​
:pin588:x3 ​ :pin590:x3 ​ :pin597:x2 ​ :pin604:x2 ​ :pin606:x2 ​ :pin615:x2 ​ :pin623:x2 ​ :pin625:x2 ​ :pin633:x2 ​ 
:pin641:x2 ​ :pin645:x3 ​ :pin648:x2 ​ :pin653:x2 ​ :pin658:x2 ​ :pin671:x2 ​ :pin675:x2 ​ :pin680:x2 ​ :pin681:x2 ​ 
:pin685:x2 ​ :pin687:x2 ​ :pin704:x2 ​ :pin705:x2 ​ :pin706:x2 ​ :pin718:x2 ​ :pin720:x2 ​ :logopin2:x2 ​ :logopin9:x2 ​
:logopin15:x2 ​ :logopin16:x2 ​ :logopin24:x2 ​ :logopin34:x3 ​ :logopin43:x2 ​ :logopin44:x2 ​ :logopin49:x2 ​ :logopin55:x2 ​ :logopin66:x2 ​ 
:logopin67:x2 ​ :logopin68:x2 ​ :logopin70:x3 ​ :logopin73:x2 ​ :logopin75:x2 ​ :logopin77:x3 ​ :logopin78:x2 ​ :logopin81:x2 ​ :logopin84:x2 ​

'''
