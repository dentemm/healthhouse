const path = require('path');
const webpack = require('webpack');

module.exports = () => {

  return {
    entry: './src/index.js',
    output: {
      path: path.resolve(__dirname, 'build'),
      filename: 'bundle.js'
    },
    module: {
      rules: [
        {
          test: /\.(js|jsx)$/,
          exclude: /node_modules/,
          use: ['babel-loader']
        }
      ]
    },
    resolve: {
      extensions: ['*', '.js', '.jsx']
    },
    devServer: {
      contentBase: './build',
      hot: true
    },
    plugins: [
      new webpack.HotModuleReplacementPlugin()
    ]
  }
};