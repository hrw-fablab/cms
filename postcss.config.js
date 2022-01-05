module.exports = {
	plugins: [
		require('postcss-dropunusedvars'),
		//require('@fullhuman/postcss-purgecss')({content: ["templates/*/*.html"],}),
		require('cssnano')({preset: 'default',})
	]
}