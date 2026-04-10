"""Script tạo file data.py chứa 1000 địa điểm du lịch Việt Nam."""
import random
import os

random.seed(42)

# 100 địa điểm gốc viết tay
hand_written = [
    {"id": 1, "name": "Vịnh Hạ Long", "description": "Di sản thiên nhiên thế giới ở Quảng Ninh với hàng ngàn hòn đảo đá vôi kỳ vĩ trên biển."},
    {"id": 2, "name": "Phố cổ Hội An", "description": "Khu phố cổ kính ở Quảng Nam với những chiếc đèn lồng, kiến trúc độc đáo và không gian yên bình đậm chất văn hóa."},
    {"id": 3, "name": "Bà Nà Hills", "description": "Khu du lịch Đà Nẵng trên vùng núi cao với Cầu Vàng, làng Pháp và thời tiết bốn mùa trong một ngày mát mẻ."},
    {"id": 4, "name": "Đảo Phú Quốc", "description": "Hòn đảo ngọc ở Kiên Giang với cát trắng, bãi biển xanh, lặn ngắm san hô và hải sản tươi ngon tuyệt vời."},
    {"id": 5, "name": "Sapa", "description": "Khám phá vùng núi Tây Bắc với ruộng bậc thang, đỉnh Phan Xi Păng mù sương và văn hóa bản địa dân tộc thiểu số."},
    {"id": 6, "name": "Cố đô Huế", "description": "Quần thể di tích lịch sử cung đình, lăng tẩm các vua nhà Nguyễn và dòng sông Hương thơ mộng."},
    {"id": 7, "name": "Động Phong Nha", "description": "Hệ thống hang động kỳ vĩ nhất thế giới ở Quảng Bình với thạch nhũ triệu năm và sông ngầm dài bất tận."},
    {"id": 8, "name": "Mũi Né", "description": "Bãi biển nổi tiếng ở Bình Thuận với đồi cát bay, lướt ván diều và hoàng hôn tuyệt đẹp trên biển."},
    {"id": 9, "name": "Đà Lạt", "description": "Thành phố ngàn hoa trên cao nguyên Lâm Đồng với khí hậu mát mẻ quanh năm, hồ Xuân Hương và vườn hoa rực rỡ."},
    {"id": 10, "name": "Ninh Bình", "description": "Tràng An với hang động, đầm Vân Long yên bình và chùa Bái Đính lớn nhất Đông Nam Á giữa núi non hùng vĩ."},
    {"id": 11, "name": "Côn Đảo", "description": "Quần đảo hoang sơ ở Bà Rịa Vũng Tàu với biển xanh trong vắt, rùa biển đẻ trứng và di tích nhà tù lịch sử."},
    {"id": 12, "name": "Cát Bà", "description": "Đảo lớn nhất vịnh Lan Hạ thuộc Hải Phòng với rừng nguyên sinh, leo núi mạo hiểm và bơi kayak giữa vịnh."},
    {"id": 13, "name": "Hồ Gươm Hà Nội", "description": "Trái tim thủ đô ngàn năm văn hiến với Tháp Rùa, đền Ngọc Sơn và cầu Thê Húc đỏ rực bên hồ xanh."},
    {"id": 14, "name": "Bãi biển Mỹ Khê", "description": "Một trong những bãi biển đẹp nhất hành tinh ở Đà Nẵng với cát trắng mịn, nước biển trong xanh và sóng nhẹ."},
    {"id": 15, "name": "Đèo Hải Vân", "description": "Con đèo hùng vĩ nối Huế và Đà Nẵng với cảnh biển núi tuyệt đẹp, được mệnh danh thiên hạ đệ nhất hùng quan."},
    {"id": 16, "name": "Chùa Một Cột", "description": "Biểu tượng kiến trúc độc đáo của Hà Nội hình bông sen nở trên mặt nước, di tích lịch sử ngàn năm."},
    {"id": 17, "name": "Cù Lao Chàm", "description": "Khu dự trữ sinh quyển thế giới ở Quảng Nam với rạn san hô đa dạng, lặn biển và làng chài yên bình."},
    {"id": 18, "name": "Tam Đảo", "description": "Thị trấn trên mây ở Vĩnh Phúc với khí hậu se lạnh, rừng thông xanh ngát và thác nước giữa núi rừng."},
    {"id": 19, "name": "Đồng bằng sông Cửu Long", "description": "Miền Tây sông nước với chợ nổi Cái Răng, vườn trái cây nhiệt đới và cuộc sống bình dị trên sông rạch."},
    {"id": 20, "name": "Hang Sơn Đoòng", "description": "Hang động lớn nhất thế giới ở Quảng Bình với rừng nguyên sinh bên trong, hố sụt khổng lồ và dòng sông ngầm."},
    {"id": 21, "name": "Vũng Tàu", "description": "Thành phố biển gần Sài Gòn với bãi Sau sầm uất, tượng Chúa Kitô trên núi và hải sản tươi sống giá rẻ."},
    {"id": 22, "name": "Phú Yên", "description": "Xứ sở hoa vàng trên cỏ xanh với gành Đá Đĩa độc đáo, bãi Xép hoang sơ và đầm Ô Loan yên tĩnh."},
    {"id": 23, "name": "Quy Nhơn", "description": "Thành phố biển Bình Định với Eo Gió, kỳ co xanh ngắt, tháp Chăm cổ và bún chả cá đặc sản."},
    {"id": 24, "name": "Lý Sơn", "description": "Đảo tiền tiêu Quảng Ngãi với cổng Tò Vò, hang Câu hùng vĩ, vườn tỏi xanh mướt và biển xanh trong vắt."},
    {"id": 25, "name": "Hà Giang", "description": "Cực Bắc Tổ quốc với cao nguyên đá Đồng Văn, đèo Mã Pí Lèng hiểm trở và sông Nho Quế xanh ngọc bích."},
    {"id": 26, "name": "Mù Cang Chải", "description": "Ruộng bậc thang mùa lúa chín vàng rực ở Yên Bái, cảnh đẹp như tranh vẽ giữa núi rừng Tây Bắc."},
    {"id": 27, "name": "Mai Châu", "description": "Thung lũng xanh tươi ở Hòa Bình với nhà sàn dân tộc Thái, múa xòe, rượu cần và không khí trong lành."},
    {"id": 28, "name": "Tây Nguyên", "description": "Vùng đất bazan với thác Dray Nur hùng vĩ, cồng chiêng Tây Nguyên, buôn làng và cà phê thơm lừng."},
    {"id": 29, "name": "Nha Trang", "description": "Thành phố biển nổi tiếng Khánh Hòa với Vinpearl Land, tháp Bà Ponagar, bãi biển dài và đời sống về đêm sôi động."},
    {"id": 30, "name": "Phong Nha - Kẻ Bàng", "description": "Vườn quốc gia di sản thế giới ở Quảng Bình với hệ thống hang động phức tạp và rừng nguyên sinh quý hiếm."},
    {"id": 31, "name": "Cầu Rồng Đà Nẵng", "description": "Cây cầu biểu tượng hình rồng ở Đà Nẵng phun lửa và nước vào cuối tuần, kỳ quan kiến trúc hiện đại."},
    {"id": 32, "name": "Chợ Bến Thành", "description": "Biểu tượng Sài Gòn với hàng trăm gian hàng bán đồ lưu niệm, ẩm thực đường phố và quần áo sầm uất."},
    {"id": 33, "name": "Núi Bà Đen", "description": "Nóc nhà Nam Bộ ở Tây Ninh với cáp treo hiện đại, chùa trên đỉnh núi và cảnh bình minh trên mây tuyệt đẹp."},
    {"id": 34, "name": "Hồ Ba Bể", "description": "Hồ nước ngọt tự nhiên lớn nhất Việt Nam ở Bắc Kạn giữa rừng nguyên sinh, chèo thuyền ngắm cảnh yên bình."},
    {"id": 35, "name": "Thác Bản Giốc", "description": "Thác nước hùng vĩ nhất Đông Nam Á nằm ở biên giới Cao Bằng với dòng nước trắng xóa đổ xuống vực sâu."},
    {"id": 36, "name": "Cố đô Hoa Lư", "description": "Kinh đô đầu tiên của Việt Nam ở Ninh Bình với đền thờ vua Đinh Tiên Hoàng và Lê Đại Hành giữa núi non."},
    {"id": 37, "name": "Phố đi bộ Nguyễn Huệ", "description": "Con phố sầm uất nhất Sài Gòn với đài phun nước, biểu diễn nghệ thuật đường phố và quán cà phê hiện đại."},
    {"id": 38, "name": "Đảo Bình Ba", "description": "Đảo tôm hùm nổi tiếng ở Khánh Hòa với nước biển trong vắt, bãi tắm đôi và hải sản tôm hùm tươi sống."},
    {"id": 39, "name": "Tam Cốc - Bích Động", "description": "Hạ Long trên cạn ở Ninh Bình với thuyền chèo len lỏi qua hang động, cánh đồng lúa và núi đá vôi."},
    {"id": 40, "name": "Bãi Dài Cam Ranh", "description": "Bãi biển dài 10km ở Khánh Hòa với cát trắng mịn, nước biển xanh ngọc và resort nghỉ dưỡng cao cấp."},
    {"id": 41, "name": "Dinh Độc Lập", "description": "Công trình kiến trúc lịch sử tại Sài Gòn, chứng nhân sự kiện thống nhất đất nước ngày 30 tháng 4 năm 1975."},
    {"id": 42, "name": "Chùa Bái Đính", "description": "Quần thể chùa lớn nhất Đông Nam Á ở Ninh Bình với tượng Phật khổng lồ, hành lang La Hán và kiến trúc đồ sộ."},
    {"id": 43, "name": "Đảo Nam Du", "description": "Quần đảo hoang sơ ở Kiên Giang với biển xanh lam, bãi cát vàng, làng chài mộc mạc và mực nướng thơm ngon."},
    {"id": 44, "name": "Suối Tiên", "description": "Khu du lịch giải trí lớn ở Sài Gòn với công viên nước, trò chơi cảm giác mạnh và kiến trúc cung đình rực rỡ."},
    {"id": 45, "name": "Cổ Thạch", "description": "Bãi đá bảy màu độc đáo ở Bình Thuận với những viên đá cuội nhiều sắc màu trải dài dọc bờ biển."},
    {"id": 46, "name": "Đường hầm đất sét Đà Lạt", "description": "Công trình nghệ thuật điêu khắc đất sét độc đáo ở Đà Lạt tái hiện các công trình kiến trúc nổi tiếng thế giới."},
    {"id": 47, "name": "Vườn quốc gia Cát Tiên", "description": "Khu bảo tồn thiên nhiên ở Đồng Nai với rừng nguyên sinh, xem đom đóm ban đêm và động vật hoang dã quý hiếm."},
    {"id": 48, "name": "Cù lao Xanh", "description": "Đảo nhỏ hoang sơ ở Quy Nhơn với ngọn hải đăng cổ trăm tuổi, rạn san hô và nước biển xanh lam."},
    {"id": 49, "name": "Đèo Ô Quy Hồ", "description": "Một trong tứ đại đỉnh đèo Tây Bắc nối Lào Cai và Lai Châu với cảnh núi rừng hùng vĩ và mây trắng bao phủ."},
    {"id": 50, "name": "Chợ nổi Cái Răng", "description": "Chợ trên sông đặc trưng miền Tây ở Cần Thơ với thuyền bán trái cây, hủ tiếu và cuộc sống sông nước nhộn nhịp."},
]

# Dữ liệu mẫu để sinh tự động các địa điểm 51-1000
provinces = [
    "Hà Nội", "Hồ Chí Minh", "Đà Nẵng", "Hải Phòng", "Cần Thơ",
    "Quảng Ninh", "Lào Cai", "Yên Bái", "Hà Giang", "Cao Bằng",
    "Lạng Sơn", "Bắc Kạn", "Thái Nguyên", "Tuyên Quang", "Phú Thọ",
    "Vĩnh Phúc", "Bắc Giang", "Bắc Ninh", "Hưng Yên", "Hải Dương",
    "Nam Định", "Thái Bình", "Ninh Bình", "Thanh Hóa", "Nghệ An",
    "Hà Tĩnh", "Quảng Bình", "Quảng Trị", "Thừa Thiên Huế", "Quảng Nam",
    "Quảng Ngãi", "Bình Định", "Phú Yên", "Khánh Hòa", "Ninh Thuận",
    "Bình Thuận", "Kon Tum", "Gia Lai", "Đắk Lắk", "Đắk Nông",
    "Lâm Đồng", "Bình Phước", "Tây Ninh", "Bình Dương", "Đồng Nai",
    "Bà Rịa Vũng Tàu", "Long An", "Tiền Giang", "Bến Tre", "Trà Vinh",
    "Vĩnh Long", "Đồng Tháp", "An Giang", "Kiên Giang", "Hậu Giang",
    "Sóc Trăng", "Bạc Liêu", "Cà Mau", "Điện Biên", "Lai Châu",
    "Sơn La", "Hòa Bình",
]

templates = [
    # Biển / Đảo
    {
        "name_templates": [
            "Bãi biển {place}", "Bãi tắm {place}", "Vịnh {place}",
            "Đảo {place}", "Bờ biển {place}", "Mũi {place}",
        ],
        "place_names": [
            "Thiên Cầm", "Đại Lãnh", "Dốc Lết", "Từ Nham", "Nhơn Lý",
            "Ghềnh Ráng", "Hòn Khô", "Hòn Nưa", "Hòn Mun", "Hòn Tằm",
            "Hòn Thơm", "Hòn Nghệ", "Hòn Sơn", "Hòn Dấu", "Trà Cổ",
            "Cửa Tùng", "Thuận An", "Cảnh Dương", "Nhật Lệ", "Đồ Sơn",
            "Sầm Sơn", "Cửa Lò", "Thiên Cầm", "Vũng Chùa", "Lăng Cô",
            "Hà My", "Tam Thanh", "Sa Huỳnh", "Đại Lãnh", "Vĩnh Hảo",
            "La Gi", "Kê Gà", "Long Hải", "Hồ Cốc", "Hồ Tràm",
            "Bãi Trước", "Bãi Dứa", "Ngọc Vừng", "Quan Lạn", "Minh Châu",
        ],
        "desc_templates": [
            "Bãi biển hoang sơ ở {province} với cát trắng mịn, nước biển trong xanh và không khí yên bình cho kỳ nghỉ thư giãn.",
            "Điểm đến biển tuyệt đẹp ở {province} với sóng nhẹ, bãi cát dài và hải sản tươi sống đa dạng phong phú.",
            "Bãi biển ít người biết ở {province} với khung cảnh hoang sơ, nước biển xanh ngọc và hoàng hôn rực rỡ mỗi chiều.",
            "Vùng biển đẹp ở {province} với san hô đa dạng, lặn ngắm cá nhiệt đới và bãi cát vàng óng ả.",
            "Bờ biển thơ mộng ở {province} với làng chài yên bình, thuyền đánh cá truyền thống và hải sản nướng thơm phức.",
            "Điểm check-in nổi tiếng ở {province} với ghềnh đá tự nhiên, sóng biển tung bọt trắng xóa và cảnh bình minh huyền ảo.",
        ],
    },
    # Núi / Đèo / Cao nguyên
    {
        "name_templates": [
            "Đỉnh {place}", "Núi {place}", "Đèo {place}",
            "Cao nguyên {place}", "Thung lũng {place}", "Đồi {place}",
        ],
        "place_names": [
            "Tà Xùa", "Tà Chì Nhù", "Lảo Thẩn", "Ky Quan San", "Nhìu Cồ San",
            "Putaleng", "Bạch Mộc Lương Tử", "Pha Luông", "Chư Yang Sin", "Langbiang",
            "Hàm Rồng", "Thiên Phúc", "Bà Nà", "Sơn Trà", "Hòn Bà",
            "Bidoup", "Ngọc Linh", "Chư Đăng Ya", "Măng Đen", "Kon Ka Kinh",
            "Mẫu Sơn", "Yên Tử", "Tam Đảo", "Ba Vì", "Bù Gia Mập",
            "Hàm Lợn", "Phia Oắc", "Phia Đén", "Chư Hreng", "Vọng Phu",
            "Cô Tiên", "Bạch Mã", "Hải Vân", "Đá Bia", "Cà Đam",
            "Chu Va", "Khau Phạ", "Lũng Cú", "Mã Pí Lèng", "Cổng Trời",
        ],
        "desc_templates": [
            "Đỉnh núi hùng vĩ ở {province} với biển mây bồng bềnh, cảnh hoàng hôn tráng lệ và không khí trong lành se lạnh.",
            "Cung đường trekking đẹp nhất {province} với rừng nguyên sinh, suối trong và đỉnh núi sương mù quanh năm.",
            "Điểm săn mây nổi tiếng ở {province} với biển mây trắng xóa lúc bình minh và cảnh núi non trùng điệp.",
            "Vùng cao nguyên mát mẻ ở {province} với đồi chè xanh mướt, rừng thông bạt ngàn và khí hậu ôn hòa quanh năm.",
            "Con đèo ngoạn mục ở {province} với cung đường uốn lượn giữa núi rừng, phong cảnh hùng vĩ ngoạn mục hai bên.",
            "Thung lũng xanh tươi ở {province} được bao bọc bởi núi non, ruộng lúa bậc thang và bản làng dân tộc yên bình.",
        ],
    },
    # Thác nước / Suối / Hồ
    {
        "name_templates": [
            "Thác {place}", "Suối {place}", "Hồ {place}",
            "Đầm {place}", "Khe {place}", "Suối nước nóng {place}",
        ],
        "place_names": [
            "Bạc", "Vàng", "Mơ", "Tình Yêu", "Đá Nhảy",
            "Trắng", "Xanh", "Tiên Sa", "Datanla", "Prenn",
            "Cam Ly", "Voi", "Dambri", "Liên Khương", "Đắk G'Lun",
            "Trinh Nữ", "Thủy Tiên", "Ngọc", "Yang Bay", "Ba Hồ",
            "Lưu Ly", "Tà Gụ", "Thác Mây", "Khe Gỗ", "Khe Nước Trong",
            "Bàu Sen", "Bàu Trắng", "Ea Kao", "Lắk", "Dầu Tiếng",
            "Trị An", "Phú Ninh", "Kẻ Gỗ", "Thác Bà", "Cấm Sơn",
            "Núi Cốc", "Đại Lải", "Suối Mỡ", "Suối Vàng", "Khoáng Kim Bôi",
        ],
        "desc_templates": [
            "Thác nước hùng vĩ ở {province} với dòng nước trắng xóa đổ từ vách đá cao giữa rừng xanh mướt nguyên sinh.",
            "Suối nước trong vắt ở {province} chảy qua những tảng đá rêu phong, lý tưởng cho tắm suối và dã ngoại cuối tuần.",
            "Hồ nước thơ mộng ở {province} bao quanh bởi đồi thông xanh, không gian yên tĩnh cho cắm trại và chèo thuyền.",
            "Khu vực suối nước nóng thiên nhiên ở {province} với nhiệt độ dễ chịu, tắm khoáng tự nhiên tốt cho sức khỏe.",
            "Dòng suối mát lành giữa rừng {province} với ghềnh đá tự nhiên tạo thành bể bơi thiên nhiên tuyệt đẹp.",
            "Đầm nước yên bình ở {province} với hoa sen nở rộ, chim muông đa dạng và cảnh hoàng hôn phản chiếu tráng lệ.",
        ],
    },
    # Chùa / Đền / Di tích lịch sử
    {
        "name_templates": [
            "Chùa {place}", "Đền {place}", "Đình {place}",
            "Miếu {place}", "Tháp {place}", "Di tích {place}",
        ],
        "place_names": [
            "Thiên Mụ", "Trấn Quốc", "Tây Phương", "Thầy", "Hương Tích",
            "Dâu", "Phật Tích", "Keo", "Bút Tháp", "Mía",
            "Linh Ứng", "Linh Phước", "Long Sơn", "Vĩnh Nghiêm", "Quốc Ân",
            "Giác Lâm", "Vĩnh Tràng", "Phổ Quang", "Tam Chúc", "Perfume",
            "Hùng Vương", "Kiếp Bạc", "Côn Sơn", "Sóc", "Trần",
            "Bạch Đằng", "Lam Kinh", "Thành Cổ Quảng Trị", "Ngã Ba Đồng Lộc", "Thành Tây Đô",
            "A Sào", "Cổ Loa", "Văn Miếu", "Hoàng Thành Thăng Long", "Thành Nhà Mạc",
            "Poh Nagar", "Dương Long", "Bình Sơn", "Mỹ Sơn B", "Chiên Đàn",
        ],
        "desc_templates": [
            "Ngôi chùa cổ kính ở {province} với kiến trúc truyền thống, tượng Phật trang nghiêm và không gian thanh tịnh yên bình.",
            "Di tích lịch sử quan trọng ở {province} ghi dấu ấn văn hóa và lịch sử hào hùng của dân tộc Việt Nam.",
            "Đền thờ linh thiêng ở {province} với kiến trúc cổ xưa, lễ hội truyền thống và không khí tâm linh tĩnh lặng.",
            "Công trình kiến trúc tôn giáo nổi bật ở {province} với tháp cổ mang dấu ấn văn hóa Chăm Pa độc đáo.",
            "Quần thể di tích văn hóa ở {province} với đền đài cổ kính, lăng tẩm hoàng gia và vườn cảnh trang nhã.",
            "Ngôi đình làng trăm tuổi ở {province} với kiến trúc gỗ điêu khắc tinh xảo, nơi lưu giữ hồn quê Việt Nam.",
        ],
    },
    # Làng nghề / Ẩm thực / Văn hóa
    {
        "name_templates": [
            "Làng nghề {place}", "Phố ẩm thực {place}", "Chợ {place}",
            "Làng văn hóa {place}", "Phố cổ {place}", "Bản {place}",
        ],
        "place_names": [
            "gốm Bát Tràng", "lụa Vạn Phúc", "tranh Đông Hồ", "nón Chuông", "đúc đồng Ngũ Xã",
            "mộc Kim Bồng", "chiếu Nga Sơn", "nước mắm Phú Quốc", "muối Bạc Liêu", "trống Đọi Tam",
            "đá Non Nước", "thêu Quất Động", "rèn Đa Sỹ", "giấy dó Yên Thái", "sơn mài Hạ Thái",
            "dệt thổ cẩm", "nón lá Huế", "hoa Đà Lạt", "cá Phan Thiết", "kẹo dừa Bến Tre",
            "đêm Tây Bùi Viện", "đêm Tạ Hiện", "đêm Đà Lạt", "đêm Phú Quốc", "đêm Hội An",
            "Tả Phìn", "Tả Van", "Lao Chải", "Cát Cát", "Sin Chai",
            "Pom Coọng", "Lác", "Bằng", "Stơr", "Kon K'Tu",
            "Mường Hum", "Mường Thanh", "Y Tý", "A Pa Chải", "Mường Lò",
        ],
        "desc_templates": [
            "Làng nghề truyền thống nổi tiếng ở {province} với kỹ thuật thủ công tinh xảo lưu truyền qua nhiều thế hệ.",
            "Khu phố ẩm thực sôi động ở {province} với đặc sản địa phương, món ăn đường phố và hương vị đậm đà khó quên.",
            "Chợ truyền thống đặc sắc ở {province} với sản vật địa phương, ẩm thực dân dã và không khí mua bán nhộn nhịp.",
            "Bản làng dân tộc thiểu số ở {province} với nhà sàn gỗ, nghề dệt thổ cẩm và nếp sống văn hóa bản địa.",
            "Không gian văn hóa truyền thống ở {province} với lễ hội dân gian, âm nhạc đặc trưng và ẩm thực dân tộc.",
            "Phố cổ rêu phong ở {province} với kiến trúc cổ kính, quán cà phê giấu kín và góc phố nghệ thuật đường phố.",
        ],
    },
    # Vườn quốc gia / Khu bảo tồn
    {
        "name_templates": [
            "Vườn quốc gia {place}", "Khu bảo tồn {place}", "Rừng {place}",
            "Khu sinh thái {place}", "Vườn thực vật {place}", "Đồng cỏ {place}",
        ],
        "place_names": [
            "Bạch Mã", "Cát Bà", "Tam Đảo", "Ba Vì", "Xuân Sơn",
            "Bến En", "Pù Mát", "Vũ Quang", "Bạch Long Vĩ", "Xuân Thủy",
            "Yok Đôn", "Chư Mom Ray", "Bidoup Núi Bà", "Lò Gò Xa Mát", "Bù Gia Mập",
            "Tràm Chim", "U Minh Thượng", "U Minh Hạ", "Mũi Cà Mau", "Phước Bình",
            "Ngọc Sơn Ngổ Luông", "Hang Kia Pà Cò", "Sốp Cộp", "Hoàng Liên", "Mường Nhé",
            "Pù Luông", "Ngọc Linh", "Đất Mũi", "Lung Ngọc Hoàng", "Láng Sen",
            "ngập mặn Cần Giờ", "ngập mặn Xuân Thủy", "tràm Trà Sư", "thông Đà Lạt", "dừa Bến Tre",
            "Đồng Nai", "Côn Đảo", "Phú Quốc", "Núi Chúa", "Cát Tiên",
        ],
        "desc_templates": [
            "Khu rừng nguyên sinh ở {province} với hệ sinh thái đa dạng, nhiều loài động thực vật quý hiếm cần được bảo tồn.",
            "Vườn quốc gia nổi tiếng ở {province} với cảnh quan thiên nhiên tuyệt đẹp, đường trekking và quan sát chim rừng.",
            "Khu bảo tồn thiên nhiên ở {province} với rừng ngập mặn phong phú, hệ sinh thái ven biển và đa dạng sinh học.",
            "Rừng nhiệt đới xanh mướt ở {province} với thảm thực vật phong phú, thác nước ẩn giấu và không khí trong lành.",
            "Khu sinh thái ven sông ở {province} với ruộng lúa xanh bạt ngàn, đàn cò trắng bay và cuộc sống nông thôn thanh bình.",
            "Vùng đất ngập nước quan trọng ở {province} với hệ sinh thái độc đáo, mùa nước nổi và đồng sen bạt ngàn.",
        ],
    },
    # Resort / Nghỉ dưỡng / Khu vui chơi
    {
        "name_templates": [
            "Khu nghỉ dưỡng {place}", "Khu du lịch {place}", "Công viên {place}",
            "Suối khoáng {place}", "Khu vui chơi {place}", "Hồ bơi vô cực {place}",
        ],
        "place_names": [
            "Bình Châu", "Thanh Tân", "Mỹ An", "Alba", "Kim Bôi",
            "Đại Lải", "Flamingo", "Emeralda", "Topas", "Victoria",
            "Amanoi", "Six Senses", "InterContinental", "Banyan Tree", "Fusion",
            "Sun World", "VinWonders", "Asia Park", "Bà Nà", "Hòn Thơm",
            "Đại Nam", "Thỏ Trắng", "Suối Tiên", "Dam Sen", "Khoang Xanh",
            "Núi Thần Tài", "Bà Đen", "Yên Tử", "Tràng An", "Champa Island",
            "Mường Thanh", "FLC", "Vinpearl", "Pullman", "Hyatt",
            "Marriott", "Four Seasons", "Park Hyatt", "Sheraton", "Novotel",
        ],
        "desc_templates": [
            "Khu nghỉ dưỡng cao cấp ở {province} với hồ bơi vô cực, spa thư giãn và tầm nhìn ra biển tuyệt đẹp.",
            "Khu du lịch sinh thái ở {province} với suối khoáng nóng thiên nhiên, tắm bùn và massage thư giãn toàn thân.",
            "Công viên giải trí hiện đại ở {province} với trò chơi cảm giác mạnh, công viên nước và khu vui chơi trẻ em.",
            "Resort ven biển sang trọng ở {province} với villa riêng biệt, bãi biển tư nhân và nhà hàng ẩm thực đa quốc gia.",
            "Khu du lịch trải nghiệm ở {province} với cáp treo, xe trượt máng và các hoạt động ngoài trời phiêu lưu mạo hiểm.",
            "Tổ hợp nghỉ dưỡng ở {province} với sân golf quốc tế, trung tâm hội nghị và khu mua sắm sầm uất.",
        ],
    },
    # Cánh đồng / Nông nghiệp / Thiên nhiên
    {
        "name_templates": [
            "Cánh đồng {place}", "Vườn {place}", "Đồi {place}",
            "Trang trại {place}", "Rẫy {place}", "Nông trại {place}",
        ],
        "place_names": [
            "lúa Tam Cốc", "lúa Mù Cang Chải", "lúa Tú Lệ", "hoa Mê Linh", "hoa Đà Lạt",
            "cúc họa mi", "tam giác mạch", "hoa cải Mộc Châu", "hướng dương", "lavender",
            "chè Thái Nguyên", "chè Mộc Châu", "chè Bảo Lộc", "cà phê Buôn Ma Thuột", "cà phê Đà Lạt",
            "tiêu Phú Quốc", "điều Bình Phước", "cao su Bình Dương", "dừa Bến Tre", "xoài Cao Lãnh",
            "bưởi Đoan Hùng", "vải Bắc Giang", "nhãn Hưng Yên", "thanh long Bình Thuận", "dâu Đà Lạt",
            "chôm chôm Bến Tre", "sầu riêng Cái Mơn", "măng cụt Lái Thiêu", "bơ Đắk Lắk", "mắc ca Tây Nguyên",
            "nho Ninh Thuận", "ổi Bến Tre", "mít Thái", "quýt hồng Lai Vung", "cam sành Hà Giang",
            "chanh Thuận Thới", "khóm Tân Phước", "sapoche Xuân Đỉnh", "dưa hấu Gia Lai", "atiso Đà Lạt",
        ],
        "desc_templates": [
            "Cánh đồng bạt ngàn ở {province} với sắc màu rực rỡ theo mùa, điểm chụp ảnh thiên nhiên tuyệt đẹp.",
            "Vườn trái cây sai quả ở {province} nơi du khách có thể tham quan, hái quả tươi và thưởng thức tại vườn.",
            "Đồi xanh mướt trải dài ở {province} với khí hậu mát mẻ, hương thơm ngào ngạt và cảnh quan bình yên thơ mộng.",
            "Trang trại sinh thái ở {province} nơi trải nghiệm cuộc sống nông thôn, thu hoạch nông sản và thưởng thức đặc sản.",
            "Vùng nông nghiệp trù phú ở {province} với sản vật đặc trưng địa phương nổi tiếng khắp cả nước.",
            "Khu vườn thiên nhiên ở {province} với không gian xanh mát, chụp ảnh sống ảo và trải nghiệm làm nông dân.",
        ],
    },
]

def generate():
    destinations = list(hand_written)  # copy 50 đầu
    used_names = {d["name"] for d in destinations}
    idx = len(destinations) + 1

    while len(destinations) < 1000:
        cat = random.choice(templates)
        name_tpl = random.choice(cat["name_templates"])
        place = random.choice(cat["place_names"])
        desc_tpl = random.choice(cat["desc_templates"])
        province = random.choice(provinces)

        name = name_tpl.format(place=place)
        if name in used_names:
            continue
        used_names.add(name)

        desc = desc_tpl.format(province=province)
        destinations.append({"id": idx, "name": name, "description": desc})
        idx += 1

    return destinations


if __name__ == "__main__":
    data = generate()
    lines = ["# Auto-generated: 1000 Địa điểm du lịch Việt Nam", "tourist_destinations = ["]
    for d in data:
        lines.append(f'    {{"id": {d["id"]}, "name": "{d["name"]}", "description": "{d["description"]}"}},')
    lines.append("]")
    lines.append("")

    out_path = os.path.join(os.path.dirname(__file__), "data.py")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Đã tạo {len(data)} địa điểm vào {out_path}")
