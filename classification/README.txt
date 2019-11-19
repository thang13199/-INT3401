
Câu 4: tạo 1 features mới giúp tăng Performance 
feature dạng True false
Ý tưởng: kiểm tra lặp lại pixel 0 ,hoặc cụm pixel bằng cách kiểm tra bên cạnh pixel 0 còn có pixel khác(!=0) cạnh nó hay không


sử dụng defth first seach để kiểm tra toàn bộ trạng thái pixel kế tiếp
	nếu vượt ra ngoài size  thì trả về false(từ lúc duyệt ban đầu đến khi tới rìa đều 	không 	xuất hiện pixel khác 0)
	xuất pixel(x,y) khác 0 thì trả về True
	nếu (x,y) đã dyueetj trả về true 
	nếu không thì đưa (x,y) vào tệp đã duyệt và không duyệt lại nữa
	(đánh dấu đã duyệt cho  (x,y))
	trả về cụm logic and của  hàm defth first seach  cho các pixel xung quanh pixel đang 	duyệt
	return dfs(x - 1, y) and dfs(x + 1, y) and dfs(x, y - 1) and dfs(x, y + 1)
	nếu tất cả đều true thì mới trả về true, chỉ cần 1 chiều mà vượt ra khỏi 	biên thì sẽ là sai: 1 false-->tất cả đều false



Khởi tạo loop là false 
duyệt tất cả pixel nếu 1 cái thả mãn dfs tức là đã có lặp loop=true
trả về giá trị loop


sau cùng gọi tên feature đó ra


Câu 5 : 
duyệt qua tất cả range( self.max_iterations)
duyệt qua tất cả tệp trainingdata

	khởi tạo 1 max score với giá trị âm vô cùng
		duyệt qua lable trong trainingdata
		tính score +=  value * weights của các feature tương ứng:[lable]			[feature]
		trả về score lớn nhất kèm lable đi kèm 
	kiểm tra maxlable nếu đã có trong trainingtables thì bỏ qua tiếp tục vòng 	lặp ngược lại thì thêm nó vào training lable 
Câu 6:
	yêu cầu: tạo cá feature cho con pacman
	feature closestfood:
	--duyệt tấy cả food, đưa ra khoảng cách giữa food và pacman lấy khoảng cách food gần 	nhất 
	gán nó cho feature closestfood
	feature closestghost :
	--duyệt tất cả ghost đưa ra khoảng cách gost gần nhất 
	đưa ra feature ghost gần nhất
	--đưa ra feature food còn lại dựa trên getnumfood


