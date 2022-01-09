module.exports = {
	plugins: [
		require('@fullhuman/postcss-purgecss')({content: ["templates/*/*.html"],}),
		require('cssnano')({preset: 'default',})
	]
}