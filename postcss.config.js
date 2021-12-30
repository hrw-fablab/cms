module.exports = {
	plugins: [
		require('postcss-dropunusedvars'),
		require('cssnano')({preset: 'default',})
	]
}