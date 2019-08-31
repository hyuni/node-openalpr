﻿{
  'targets': [
    {
      'target_name': '<(module_name)',
      'sources': [
            "src/node_openalpr.cc"
      ],
	  'include_dirs': [
			"<!(node -e \"require('nan')\")",
			"includes/",
			"lib/"
	  ],
      'conditions': [
			['OS=="win"', {
				'libraries': [ '<!@(["python", "tools/getSourceFiles.py", "lib", "lib"])' ],
				'dll_files': [ '<!@(["python", "tools/getSourceFiles.py", "lib", "dll"])' ],
				'msvs_settings': {
					'VCCLCompilerTool': {
						'AdditionalOptions': [
							'/GR',
							'/MD',
							'/EHsc'
						]
					}
				}
			}],
			['OS=="darwin"', {
            	'libraries': [ "/usr/local/lib/libopenalpr-static.a" ]
            }],
			['OS=="linux"', {
				'libraries': [ "/usr/lib/libopenalpr.so" ]
			}]
      ]
    },
	{
	  "target_name": "action_after_build",
	  "type": "none",
	  "dependencies": [ "<(module_name)" ],
	  "copies": [
		{
		  "files": [ "<(PRODUCT_DIR)/<(module_name).node" ],
		  "destination": "<(module_path)"
		}
	  ]
	}
  ]
}
