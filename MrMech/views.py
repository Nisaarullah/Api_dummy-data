from rest_framework.response import Response
from rest_framework.views import APIView

class CategoryList(APIView):
    def get(self, request):
        cards = []

        card_data = [
            {
                'title': 'Book appointment at workshop',
                'description': 'User can book appointment and avail service at workshop',
                'image': 'https://unsplash.com/photos/Fd6osyVbtG4',
                'categories': [
                    {
                        'title': 'Engine',
                        'description': 'Category 1 Description',
                        'image': 'category_image_1.jpg',
                        'services': [
                            {
                                'title': 'Engine Diagnostics',
                                'price': 10.00,
                                'image': 'service_image_1.jpg',
                                'description': ' Identify issues using diagnostic tools.'
                            },
                            {
                                'title': 'Engine Tune-up',
                                'price': 15.00,
                                'image': 'service_image_2.jpg',
                                'description': 'Adjust components for optimal performance.'
                            },
                            {
                                'title': 'Timing Belt Replacement',
                                'price': 15.00,
                                'image': 'service_image_2.jpg',
                                'description': 'Replace worn timing belts.'
                            },
                            # Add more services for Category 1...
                        ]
                    },
                    {
                        'title': 'Category 2 Title',
                        'description': 'Category 2 Description',
                        'image': 'category_image_2.jpg',
                        'services': [
                            {
                                
                                'title': 'Service 3 Title',
                                'price': 20.00,
                                'image': 'service_image_3.jpg',
                                'description': 'Service 3 Description'
                            },
                            {
                               
                                'title': 'Service 4 Title',
                                'price': 25.00,
                                'image': 'service_image_4.jpg',
                                'description': 'Service 4 Description'
                            },
                            # Add more services for Category 2...
                        ]
                    },
                    {
                        'title': 'Category 2 Title',
                        'description': 'Category 2 Description',
                        'image': 'category_image_2.jpg',
                        'services': [
                            {
                                'name': 'Service 3 Name',
                                'title': 'Service 3 Title',
                                'price': 20.00,
                                'image': 'service_image_3.jpg',
                                'description': 'Service 3 Description'
                            },
                            {
                                'name': 'Service 4 Name',
                                'title': 'Service 4 Title',
                                'price': 25.00,
                                'image': 'service_image_4.jpg',
                                'description': 'Service 4 Description'
                            },
                            # Add more services for Category 2...
                        ]
                    },
                    {
                        'title': 'Category 2 Title',
                        'description': 'Category 2 Description',
                        'image': 'category_image_2.jpg',
                        'services': [
                            {
                                'name': 'Service 3 Name',
                                'title': 'Service 3 Title',
                                'price': 20.00,
                                'image': 'service_image_3.jpg',
                                'description': 'Service 3 Description'
                            },
                            {
                                'name': 'Service 4 Name',
                                'title': 'Service 4 Title',
                                'price': 25.00,
                                'image': 'service_image_4.jpg',
                                'description': 'Service 4 Description'
                            },
                            # Add more services for Category 2...
                        ]
                    },
                    {
                        'title': 'Category 2 Title',
                        'description': 'Category 2 Description',
                        'image': 'category_image_2.jpg',
                        'services': [
                            {
                                'name': 'Service 3 Name',
                                'title': 'Service 3 Title',
                                'price': 20.00,
                                'image': 'service_image_3.jpg',
                                'description': 'Service 3 Description'
                            },
                            {
                                'name': 'Service 4 Name',
                                'title': 'Service 4 Title',
                                'price': 25.00,
                                'image': 'service_image_4.jpg',
                                'description': 'Service 4 Description'
                            },
                            # Add more services for Category 2...
                        ]
                    },
                    {
                        'title': 'Category 2 Title',
                        'description': 'Category 2 Description',
                        'image': 'category_image_2.jpg',
                        'services': [
                            {
                                'name': 'Service 3 Name',
                                'title': 'Service 3 Title',
                                'price': 20.00,
                                'image': 'service_image_3.jpg',
                                'description': 'Service 3 Description'
                            },
                            {
                                'name': 'Service 4 Name',
                                'title': 'Service 4 Title',
                                'price': 25.00,
                                'image': 'service_image_4.jpg',
                                'description': 'Service 4 Description'
                            },
                            # Add more services for Category 2...
                        ]
                    },
                    {
                        'title': 'Category 2 Title',
                        'description': 'Category 2 Description',
                        'image': 'category_image_2.jpg',
                        'services': [
                            {
                                'name': 'Service 3 Name',
                                'title': 'Service 3 Title',
                                'price': 20.00,
                                'image': 'service_image_3.jpg',
                                'description': 'Service 3 Description'
                            },
                            {
                                'name': 'Service 4 Name',
                                'title': 'Service 4 Title',
                                'price': 25.00,
                                'image': 'service_image_4.jpg',
                                'description': 'Service 4 Description'
                            },
                            # Add more services for Category 2...
                        ]
                    },
                    {
                        'title': 'Category 2 Title',
                        'description': 'Category 2 Description',
                        'image': 'category_image_2.jpg',
                        'services': [
                            {
                                'name': 'Service 3 Name',
                                'title': 'Service 3 Title',
                                'price': 20.00,
                                'image': 'service_image_3.jpg',
                                'description': 'Service 3 Description'
                            },
                            {
                                'name': 'Service 4 Name',
                                'title': 'Service 4 Title',
                                'price': 25.00,
                                'image': 'service_image_4.jpg',
                                'description': 'Service 4 Description'
                            },
                            # Add more services for Category 2...
                        ]
                    },
                    {
                        'title': 'Category 2 Title',
                        'description': 'Category 2 Description',
                        'image': 'category_image_2.jpg',
                        'services': [
                            {
                                'name': 'Service 3 Name',
                                'title': 'Service 3 Title',
                                'price': 20.00,
                                'image': 'service_image_3.jpg',
                                'description': 'Service 3 Description'
                            },
                            {
                                'name': 'Service 4 Name',
                                'title': 'Service 4 Title',
                                'price': 25.00,
                                'image': 'service_image_4.jpg',
                                'description': 'Service 4 Description'
                            },
                            # Add more services for Category 2...
                        ]
                    },
                    {
                        'title': 'Category 2 Title',
                        'description': 'Category 2 Description',
                        'image': 'category_image_2.jpg',
                        'services': [
                            {
                                'name': 'Service 3 Name',
                                'title': 'Service 3 Title',
                                'price': 20.00,
                                'image': 'service_image_3.jpg',
                                'description': 'Service 3 Description'
                            },
                            {
                                'name': 'Service 4 Name',
                                'title': 'Service 4 Title',
                                'price': 25.00,
                                'image': 'service_image_4.jpg',
                                'description': 'Service 4 Description'
                            },
                            # Add more services for Category 2...
                        ]
                    },
                  
                ]
            },
             {
                'title': 'Services at your door-step',
                'description': 'Card One Description',
                'image': 'card_image_1.jpg',
                'categories': [
                    {
                        'title': 'Category 1 Title',
                        'description': 'Category 1 Description',
                        'image': 'category_image_1.jpg',
                        'services': [
                            {
                                'name': 'Service 1 Name',
                                'title': 'Service 1 Title',
                                'price': 10.00,
                                'image': 'service_image_1.jpg',
                                'description': 'Service 1 Description'
                            },
                            {
                                'name': 'Service 2 Name',
                                'title': 'Service 2 Title',
                                'price': 15.00,
                                'image': 'service_image_2.jpg',
                                'description': 'Service 2 Description'
                            },
                           
                        ]
                    },
                    {
                        'title': 'Category 2 Title',
                        'description': 'Category 2 Description',
                        'image': 'category_image_2.jpg',
                        'services': [
                            {
                                'name': 'Service 3 Name',
                                'title': 'Service 3 Title',
                                'price': 20.00,
                                'image': 'service_image_3.jpg',
                                'description': 'Service 3 Description'
                            },
                            {
                                'name': 'Service 4 Name',
                                'title': 'Service 4 Title',
                                'price': 25.00,
                                'image': 'service_image_4.jpg',
                                'description': 'Service 4 Description'
                            },
                            # Add more services for Category 2...
                        ]
                    },
                     {
                        'title': 'Category 2 Title',
                        'description': 'Category 2 Description',
                        'image': 'category_image_2.jpg',
                        'services': [
                            {
                                'name': 'Service 3 Name',
                                'title': 'Service 3 Title',
                                'price': 20.00,
                                'image': 'service_image_3.jpg',
                                'description': 'Service 3 Description'
                            },
                            {
                                'name': 'Service 4 Name',
                                'title': 'Service 4 Title',
                                'price': 25.00,
                                'image': 'service_image_4.jpg',
                                'description': 'Service 4 Description'
                            },
                            # Add more services for Category 2...
                        ]
                    },
                     {
                        'title': 'Category 2 Title',
                        'description': 'Category 2 Description',
                        'image': 'category_image_2.jpg',
                        'services': [
                            {
                                'name': 'Service 3 Name',
                                'title': 'Service 3 Title',
                                'price': 20.00,
                                'image': 'service_image_3.jpg',
                                'description': 'Service 3 Description'
                            },
                            {
                                'name': 'Service 4 Name',
                                'title': 'Service 4 Title',
                                'price': 25.00,
                                'image': 'service_image_4.jpg',
                                'description': 'Service 4 Description'
                            },
                            # Add more services for Category 2...
                        ]
                    },
                     {
                        'title': 'Category 2 Title',
                        'description': 'Category 2 Description',
                        'image': 'category_image_2.jpg',
                        'services': [
                            {
                                'name': 'Service 3 Name',
                                'title': 'Service 3 Title',
                                'price': 20.00,
                                'image': 'service_image_3.jpg',
                                'description': 'Service 3 Description'
                            },
                            {
                                'name': 'Service 4 Name',
                                'title': 'Service 4 Title',
                                'price': 25.00,
                                'image': 'service_image_4.jpg',
                                'description': 'Service 4 Description'
                            },
                            # Add more services for Category 2...
                        ]
                    },
                     {
                        'title': 'Category 2 Title',
                        'description': 'Category 2 Description',
                        'image': 'category_image_2.jpg',
                        'services': [
                            {
                                'name': 'Service 3 Name',
                                'title': 'Service 3 Title',
                                'price': 20.00,
                                'image': 'service_image_3.jpg',
                                'description': 'Service 3 Description'
                            },
                            {
                                'name': 'Service 4 Name',
                                'title': 'Service 4 Title',
                                'price': 25.00,
                                'image': 'service_image_4.jpg',
                                'description': 'Service 4 Description'
                            },
                            # Add more services for Category 2...
                        ]
                    },
                     {
                        'title': 'Category 2 Title',
                        'description': 'Category 2 Description',
                        'image': 'category_image_2.jpg',
                        'services': [
                            {
                                'name': 'Service 3 Name',
                                'title': 'Service 3 Title',
                                'price': 20.00,
                                'image': 'service_image_3.jpg',
                                'description': 'Service 3 Description'
                            },
                            {
                                'name': 'Service 4 Name',
                                'title': 'Service 4 Title',
                                'price': 25.00,
                                'image': 'service_image_4.jpg',
                                'description': 'Service 4 Description'
                            },
                            # Add more services for Category 2...
                        ]
                    },
                     {
                        'title': 'Category 2 Title',
                        'description': 'Category 2 Description',
                        'image': 'category_image_2.jpg',
                        'services': [
                            {
                                'name': 'Service 3 Name',
                                'title': 'Service 3 Title',
                                'price': 20.00,
                                'image': 'service_image_3.jpg',
                                'description': 'Service 3 Description'
                            },
                            {
                                'name': 'Service 4 Name',
                                'title': 'Service 4 Title',
                                'price': 25.00,
                                'image': 'service_image_4.jpg',
                                'description': 'Service 4 Description'
                            },
                            # Add more services for Category 2...
                        ]
                    },
                     {
                        'title': 'Category 2 Title',
                        'description': 'Category 2 Description',
                        'image': 'category_image_2.jpg',
                        'services': [
                            {
                                'name': 'Service 3 Name',
                                'title': 'Service 3 Title',
                                'price': 20.00,
                                'image': 'service_image_3.jpg',
                                'description': 'Service 3 Description'
                            },
                            {
                                'name': 'Service 4 Name',
                                'title': 'Service 4 Title',
                                'price': 25.00,
                                'image': 'service_image_4.jpg',
                                'description': 'Service 4 Description'
                            },
                            # Add more services for Category 2...
                        ]
                    },
                     {
                        'title': 'Category 2 Title',
                        'description': 'Category 2 Description',
                        'image': 'category_image_2.jpg',
                        'services': [
                            {
                                'name': 'Service 3 Name',
                                'title': 'Service 3 Title',
                                'price': 20.00,
                                'image': 'service_image_3.jpg',
                                'description': 'Service 3 Description'
                            },
                            {
                                'name': 'Service 4 Name',
                                'title': 'Service 4 Title',
                                'price': 25.00,
                                'image': 'service_image_4.jpg',
                                'description': 'Service 4 Description'
                            },
                            # Add more services for Category 2...
                        ]
                    },
                   
                ]
            },
             {
                'title': 'Card One Title',
                'description': 'Card One Description',
                'image': 'card_image_1.jpg',
                'categories': [
                    {
                        'title': 'Category 1 Title',
                        'description': 'Category 1 Description',
                        'image': 'category_image_1.jpg',
                        'services': [
                            {
                                'name': 'Service 1 Name',
                                'title': 'Service 1 Title',
                                'price': 10.00,
                                'image': 'service_image_1.jpg',
                                'description': 'Service 1 Description'
                            },
                            {
                                'name': 'Service 2 Name',
                                'title': 'Service 2 Title',
                                'price': 15.00,
                                'image': 'service_image_2.jpg',
                                'description': 'Service 2 Description'
                            },
                            
                        ]
                    },
                    {
                        'title': 'Category 2 Title',
                        'description': 'Category 2 Description',
                        'image': 'category_image_2.jpg',
                        'services': [
                            {
                                'name': 'Service 3 Name',
                                'title': 'Service 3 Title',
                                'price': 20.00,
                                'image': 'service_image_3.jpg',
                                'description': 'Service 3 Description'
                            },
                            {
                                'name': 'Service 4 Name',
                                'title': 'Service 4 Title',
                                'price': 25.00,
                                'image': 'service_image_4.jpg',
                                'description': 'Service 4 Description'
                            },
                            # Add more services for Category 2...
                        ]
                    },
                     {
                        'title': 'Category 2 Title',
                        'description': 'Category 2 Description',
                        'image': 'category_image_2.jpg',
                        'services': [
                            {
                                'name': 'Service 3 Name',
                                'title': 'Service 3 Title',
                                'price': 20.00,
                                'image': 'service_image_3.jpg',
                                'description': 'Service 3 Description'
                            },
                            {
                                'name': 'Service 4 Name',
                                'title': 'Service 4 Title',
                                'price': 25.00,
                                'image': 'service_image_4.jpg',
                                'description': 'Service 4 Description'
                            },
                            # Add more services for Category 2...
                        ]
                    },
                     {
                        'title': 'Category 2 Title',
                        'description': 'Category 2 Description',
                        'image': 'category_image_2.jpg',
                        'services': [
                            {
                                'name': 'Service 3 Name',
                                'title': 'Service 3 Title',
                                'price': 20.00,
                                'image': 'service_image_3.jpg',
                                'description': 'Service 3 Description'
                            },
                            {
                                'name': 'Service 4 Name',
                                'title': 'Service 4 Title',
                                'price': 25.00,
                                'image': 'service_image_4.jpg',
                                'description': 'Service 4 Description'
                            },
                            # Add more services for Category 2...
                        ]
                    },
                     {
                        'title': 'Category 2 Title',
                        'description': 'Category 2 Description',
                        'image': 'category_image_2.jpg',
                        'services': [
                            {
                                'name': 'Service 3 Name',
                                'title': 'Service 3 Title',
                                'price': 20.00,
                                'image': 'service_image_3.jpg',
                                'description': 'Service 3 Description'
                            },
                            {
                                'name': 'Service 4 Name',
                                'title': 'Service 4 Title',
                                'price': 25.00,
                                'image': 'service_image_4.jpg',
                                'description': 'Service 4 Description'
                            },
                            # Add more services for Category 2...
                        ]
                    },
                     {
                        'title': 'Category 2 Title',
                        'description': 'Category 2 Description',
                        'image': 'category_image_2.jpg',
                        'services': [
                            {
                                'name': 'Service 3 Name',
                                'title': 'Service 3 Title',
                                'price': 20.00,
                                'image': 'service_image_3.jpg',
                                'description': 'Service 3 Description'
                            },
                            {
                                'name': 'Service 4 Name',
                                'title': 'Service 4 Title',
                                'price': 25.00,
                                'image': 'service_image_4.jpg',
                                'description': 'Service 4 Description'
                            },
                            # Add more services for Category 2...
                        ]
                    },
                     {
                        'title': 'Category 2 Title',
                        'description': 'Category 2 Description',
                        'image': 'category_image_2.jpg',
                        'services': [
                            {
                                'name': 'Service 3 Name',
                                'title': 'Service 3 Title',
                                'price': 20.00,
                                'image': 'service_image_3.jpg',
                                'description': 'Service 3 Description'
                            },
                            {
                                'name': 'Service 4 Name',
                                'title': 'Service 4 Title',
                                'price': 25.00,
                                'image': 'service_image_4.jpg',
                                'description': 'Service 4 Description'
                            },
                            # Add more services for Category 2...
                        ]
                    },
                     {
                        'title': 'Category 2 Title',
                        'description': 'Category 2 Description',
                        'image': 'category_image_2.jpg',
                        'services': [
                            {
                                'name': 'Service 3 Name',
                                'title': 'Service 3 Title',
                                'price': 20.00,
                                'image': 'service_image_3.jpg',
                                'description': 'Service 3 Description'
                            },
                            {
                                'name': 'Service 4 Name',
                                'title': 'Service 4 Title',
                                'price': 25.00,
                                'image': 'service_image_4.jpg',
                                'description': 'Service 4 Description'
                            },
                            # Add more services for Category 2...
                        ]
                    },
                     {
                        'title': 'Category 2 Title',
                        'description': 'Category 2 Description',
                        'image': 'category_image_2.jpg',
                        'services': [
                            {
                                'name': 'Service 3 Name',
                                'title': 'Service 3 Title',
                                'price': 20.00,
                                'image': 'service_image_3.jpg',
                                'description': 'Service 3 Description'
                            },
                            {
                                'name': 'Service 4 Name',
                                'title': 'Service 4 Title',
                                'price': 25.00,
                                'image': 'service_image_4.jpg',
                                'description': 'Service 4 Description'
                            },
                            # Add more services for Category 2...
                        ]
                    },
                     {
                        'title': 'Category 2 Title',
                        'description': 'Category 2 Description',
                        'image': 'category_image_2.jpg',
                        'services': [
                            {
                                'name': 'Service 3 Name',
                                'title': 'Service 3 Title',
                                'price': 20.00,
                                'image': 'service_image_3.jpg',
                                'description': 'Service 3 Description'
                            },
                            {
                                'name': 'Service 4 Name',
                                'title': 'Service 4 Title',
                                'price': 25.00,
                                'image': 'service_image_4.jpg',
                                'description': 'Service 4 Description'
                            },
                            # Add more services for Category 2...
                        ]
                    },
                     {
                        'title': 'Category 2 Title',
                        'description': 'Category 2 Description',
                        'image': 'category_image_2.jpg',
                        'services': [
                            {
                                'name': 'Service 3 Name',
                                'title': 'Service 3 Title',
                                'price': 20.00,
                                'image': 'service_image_3.jpg',
                                'description': 'Service 3 Description'
                            },
                            {
                                'name': 'Service 4 Name',
                                'title': 'Service 4 Title',
                                'price': 25.00,
                                'image': 'service_image_4.jpg',
                                'description': 'Service 4 Description'
                            },
                            # Add more services for Category 2...
                        ]
                    },
                    # Add more categories for Card 1...
                ]
            },
           
        ]

        for card_info in card_data:
            card = {
                'title': card_info['title'],
                'image': card_info['image'],
                'description': card_info['description'],
                'categories': []
            }

            for category_info in card_info['categories']:
                category = {
                    'title': category_info['title'],
                    'image': category_info['image'],
                    'description': category_info['description'],
                    'services': []
                }

                for service_info in category_info['services']:
                    service = {
                        'title': service_info['title'],
                        'price': service_info['price'],
                        'image': service_info['image'],
                        'description': service_info['description']
                    }
                    category['services'].append(service)

                card['categories'].append(category)

            cards.append(card)

        return Response(cards)
