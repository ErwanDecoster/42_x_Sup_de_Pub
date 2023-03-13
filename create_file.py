import datetime
import json

# data = json.load(open('file.json', encoding='utf-8'))

data = [
	{
		'prenom': 'florence',
		'nom': 'foresti',
		'categorie': 'humour',
		'titre': 'Boys Boys Boys !',
		'text_preview': 'Elle revient avec son nouveau seule-en-scène intitulé Boys Boys Boys...',
		'full_text': [
			'<b>Florence Foresti</b> revient avec son <b>nouveau seule-en-scène</b> intitulé <b>Boys Boys Boys</b>, </i>“un spectacle qui croque l’époque avec justesse et drôlerie”</i>. (Télérama).',
			'<i>“Avec son incroyable énergie, son sens aigu du rythme et de la formule, Florence Foresti capte l’attention et déclenche l’hilarité.”</i> (Le Monde)',
			'À l’heure où “les <b>femmes</b> n’ont plus besoin des hommes”, mais “juste envie” pour celles qui le souhaitent, elle viendra sur la scène du <b>Grand théâtre</b> leur livrer une <b>magnifique déclaration d’amour.</b>'
		],
		'dates': [
			{
				'tarif': 62,
				'date': int(datetime.datetime(hour=21, minute=45, day=25, month=6, year=2023).timestamp())
			},
			{
				'tarif': 62,
				'date': int(datetime.datetime(hour=21, minute=45, day=26, month=6, year=2023).timestamp())
			}
		],
		'background_cotent': '',
		'images':
		[
			{
				'url': 'img_1',
				'text': 'Lorem ipsum dolor sit amet'
			},
			{
				'url': 'img_2',
				'text': 'Lorem ipsum dolor sit amet'
			},
			{
				'url': 'img_3',
				'text': 'Lorem ipsum dolor sit amet'
			},
		],
		'social_network': [
			{
				'icon': 'instagram',
				'lien': 'https://www.instagram.com/madameforesti',
			},
			{
				'icon': 'twitter',
				'lien': 'https://twitter.com/oocforesti',
			}
		],
	},
]

json.dump(data, open('file.json', 'w', encoding='utf-8'), indent=2, ensure_ascii=False)
