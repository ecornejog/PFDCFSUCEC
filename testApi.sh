echo "Test case 1  :"
echo ""
echo "testing amount= -2000"
curl --header "Content-Type: application/json" --request POST --data '{"amount":-2000}' http://localhost:5000/api/v1/startCalcul
echo ""
echo ""
echo ""



echo "Test case 2 :  http://localhost:5000/api/v1/startCalcul     '{\"amount\":5000}'" 
echo ""
curl --header "Content-Type: application/json" --request POST --data '{"amount":5000}' http://localhost:5000/api/v1/startCalcul

#echo "guid = $res1"
echo ""
echo ""
echo ""





#echo "Testing for guid=522fefjkerfkejje"

echo "Test case 3 : Sending guid not found  = 522fefjkerfkejje"
echo ""
curl http://localhost:5000/api/v1/consultStatus/522fefjkerfkejje


