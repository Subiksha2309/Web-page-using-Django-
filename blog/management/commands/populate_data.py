from typing import Any
from blog.models import FoodRecipe
from django.core.management import BaseCommand


class Command(BaseCommand):
    help="This command insert the Food Details"
    
    def handle(self, *args: Any, **options: Any):
        
        name=[
            'Dosa',
            'Idly',
            'Pongal',
            'Poori',
            'Veg Biriyani',
            'Lemon Rice',
            'Curd Rice',
            'Veg Meals',
            'Chicken Biriyani',
            'Mutton Biriyani',
            'Chicken Gravy',
            'Fish fry',
            'Mutton Gravy',
            'Chicken Fry'
    
        ]
       
        img_url=[
            'https://media.istockphoto.com/id/475689214/photo/dosa.jpg?s=612x612&w=0&k=20&c=X-cHFbMDwUHbE6tFWzZETaTzuDGRD9rJHPX1JZ0W7yY=',
            'https://media.istockphoto.com/id/174233986/photo/sambar-idli.jpg?s=612x612&w=0&k=20&c=aY5J4NGoHPNcCNScii7RWooRSIzTjwssyVWoqHZ8-R4=',
            'https://media.gettyimages.com/id/623637758/photo/white-pongal.jpg?s=612x612&w=0&k=20&c=zkIlyN5IX1XrbpQqp9DMhu4_zI68YWWHt9haVFiKACQ=',
            'https://t3.ftcdn.net/jpg/05/27/74/24/360_F_527742446_jLu7mDKK1Qx38xppfJZhDxWbBd2jTJAG.jpg',
            'https://media.gettyimages.com/id/169863606/photo/biryani.jpg?s=612x612&w=0&k=20&c=v9thOQoCHaBLF8e9plzIjT18ZnSwNkqwdVp3SVFmsgA=',
            'https://www.indianhealthyrecipes.com/wp-content/uploads/2022/02/lemon-rice.webp',
            'https://t3.ftcdn.net/jpg/04/32/15/06/360_F_432150676_TaMGOTJkQJAGHvkfrIaLvmvK88iGSsEl.jpg',
            'https://rakskitchen.net/wp-content/uploads/2013/08/9634876480_20d7ac8196_o.jpg',
            'https://media.gettyimages.com/id/1244769217/photo/chicken-dum-biryani-in-toronto-ontario-canada-on-november-12-2022.jpg?s=612x612&w=0&k=20&c=d0k_IB_1Jpa8aQjjNA_gMnFP1FvMHfHprjTZQQp4zeI=',
            'https://img.freepik.com/premium-photo/layered-mutton-biryani-with-blend-spices_1179130-437180.jpg?size=626&ext=jpg',
            'https://www.yummytummyaarthi.com/wp-content/uploads/2022/06/chicken-gravy-36.jpeg',
            'https://t3.ftcdn.net/jpg/01/71/58/86/360_F_171588688_DNG0AqpBzypIDpqnM6jb5r7Rv6JO4H67.jpg',
            'https://yummyindiankitchen.com/wp-content/uploads/2016/05/how-to-make-mutton-gravy.jpg',
            'https://www.yummytummyaarthi.com/wp-content/uploads/2017/06/1-6.jpg',
            
            
        ]

        description=[
            ' A popular South Indian dish, often served with chutney and sambar.',
            'Soft, fluffy, steamed cakes made from fermented rice and urad dal batter.',
            'A creamy and savory rice and moong dal dish garnished with cashews and pepper.',
            'Puffed, golden-brown, deep-fried bread made from wheat flour.',
            'Fragrant basmati rice cooked with mixed vegetables, spices, and herbs.',
            'Tangy rice dish flavored with lemon juice and spices.',
            'Creamy rice mixed with yogurt and tempered with spices.',
            'A traditional South Indian meal with rice, sambar, rasam, vegetables, and curd.',
            ' A rich and aromatic rice dish with marinated chicken and spices.',
            'A flavorful and hearty rice dish with tender mutton and spices.',
            'A spicy and rich gravy made with chicken and spices.',
            'Crispy and spiced fried fish.',
            ' A rich and spicy mutton curry.',
            'Spiced and crispy fried chicken.',
        ]


        ingredients=[
            'Rice, Urad dal (split black gram), Fenugreek seeds,Salt',
            'Rice, Urad dal, Fenugreek seeds, Salt',
            'Rice, Moong dal (split yellow lentils), Ghee ,Black pepper, Cumin seeds, Cashews, Curry leaves',
            'Wheat flour, Salt, Water, Oil for frying',
            'Basmati rice, Mixed vegetables (carrots, beans, peas, etc.), Onion, Tomato, Ginger-garlic paste,Biriyani masala, Mint and cilantro, Ghee or oil',
            ' Rice, lemon juice, turmeric, mustard seeds, curry leaves, peanuts, green chilies, salt.',
            'Rice, yogurt, mustard seeds, curry leaves, ginger, green chilies, coriander, salt.',
            'Rice, sambar (lentils, tamarind, spices), rasam (spiced broth), vegetables, curd.',
            'Basmati rice, chicken, yogurt, onions, tomatoes, biryani masala, saffron, ghee, mint, coriander.',
            ' Basmati rice, mutton, yogurt, onions, tomatoes, biryani masala, saffron, ghee, mint, coriander',
            'Chicken, onions, tomatoes, ginger-garlic paste, spices (turmeric, chili powder, garam masala), coriander.',
            'Fish fillets, turmeric, chili powder, salt, lemon juice, oil.',
            ' Mutton, onions, tomatoes, ginger-garlic paste, spices (turmeric, chili powder, garam masala), coriander.',
            'Chicken pieces, turmeric, chili powder, garam masala, salt, lemon juice, oil.',

       ]

        method =[
            'Soak rice and urad dal separately, grind them into a smooth batter, and allow it to ferment overnight. Spread the batter on a hot griddle, drizzle some oil, and cook until crispy.',
            'Soak rice and urad dal separately, grind them into a smooth batter, and allow it to ferment. Pour the batter into idly molds and steam for about 10-15 minutes.',
            'Cook rice and moong dal together with water until soft. In a pan, heat ghee and add cumin, black pepper, ginger, cashews, and curry leaves, then mix with the cooked rice and dal.',
            'Knead wheat flour with water to form a soft dough. Roll into small discs and deep fry until golden and puffed.',
            'Cook rice separately, prepare a vegetable mixture with spices, layer the rice and vegetables, and cook on low heat.',
            'Cook rice, temper with spices, add lemon juice, and mix well.',
            'Mix cooked rice with yogurt, temper with spices, and garnish with coriander.',
            ' Cook rice, prepare sambar, rasam, and vegetable dishes separately, serve with curd.',
            'Marinate chicken, cook rice separately, layer with chicken and rice, and cook on low heat.',
            'Marinate mutton, cook rice separately, layer with mutton and rice, and cook on low heat',
            'Sauté onions and spices, add chicken, cook until done, and garnish with coriander.',
            'Marinate fish with spices, shallow fry until crispy and golden.',
            'Sauté onions and spices, add mutton, cook until tender, and garnish with coriander.',
            'Marinate chicken with spices, shallow fry until crispy and golden.',
        ]

       
        category=[
            'VEG',
            'VEG',
            'VEG',
            'VEG',
            'VEG',
            'VEG',
            'VEG',
            'VEG',
            'NON_VEG',
            'NON_VEG',
            'NON_VEG',
            'NON_VEG',
            'NON_VEG',    
            'NON_VEG',
        ]

        for name, img_url, description, ingredients, method,category in zip(name, img_url, description, ingredients, method,category):
            
            FoodRecipe.objects.create(
                name=name,
                img_url=img_url,
                description=description,
                ingredients=ingredients,
                method=method,
                category=category
            )

    
     
        self.stdout.write(self.style.SUCCESS("Data inserted successfully"))