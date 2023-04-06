apps = [
        {
            "id": 1,
            "key": "app_",
            "image_path": b'iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAKaklEQVR4nCXW+48d5X3A4c/3fd+ZMzPnumev9tprLzi2wWCMjQi1GxzRFlDaJIogJWmV/oBUVa2iKBFN09KLUNU00DRVFZpIlXpXVVUhJG2DSgPUgEtCKcZcTDB4bYPXa+96L2fP2XObMzPv+/aHPH/FI+sXT08rm/ddUEPyFNEFKstxWLyOe9oXOB0GEpWOV7c3jvXOLx1c+cHTu3zfTVRvO4KJ/Fpy4MAlqdfPjNbXXiLrncS5XIIqDLsVghhKCR6P2D4+G4Apl6V1/hW8jkCHIBaTtUDHOClhOpcpwuZnzczUb5hyeOeFb/6dXPr2k8SVeXSzTrh3B3pbjG9tMve5T1O5bdoVq/nJbFD8tR4s/6tKpvBKITrA+QGqGGHDWehdQNYvv1uxQbkXDJbxyRjeKcCi09Y9eL6hp3cdsNbyxmd+l4tP/zP7bvsMe/74QfJGQPbOIn56jq2FBYq33qd55Ajjv3yQorgCaf2Mr04/pLpXn1XK4KJxJO3g3Qbe+opR/TV82EPyESrr4DHg0t/X2cafSNLEMeT8H/4Tq08/wf6pY8w8cDd2R4WwZKjce4hsdUB1/jCtRsLyI3+P9D/O5G/diN1av9m2s2cEHiaMvqbyNpKvg9vAyQRG8gHaCkVtCuP6EJjH9aj4vJEc26zQeu4Ui9/8W6anj7Dtc5/A3LITGRZYr0ndEFMa4dIhjTtvQb7saT/5PMntc4TzVcxgRFGZ+lOsnRL0l5yO8S4CyVE2aWLDMlLkeMKHra59PgvHKWqz+LDG4pMnUVimjx6BQ/PomTFUHCClAOUUhAlSH8OmGeVfuh012WDrhYu4sTlsXMZ7C95+0UZjX3GmBrqMDysorIj4HESOofRXJW+jiwHelBkub9F78xzjtTlKH5pDymASkMSgcUioIaqg4whtC7RyhAf30D37AaqziTiHOIcLy5CuPaqK7h2UxsEnolReDL2ugjffQUDnKagKXpVQbkROQGELxHtEJXipoH2Ith5xOX40hLiEmaqhfQECrqzQ9TKiY3AalVlUnkNQ+54LGqjB+lD5uFyg3SfNcHk7RYYLG4jto32b0evv4S58gJqsYVJL/9RF2qd/QlDXSCPG6hjTqJEvrrD6/ZPkC0uUZmoMN9fIrIYoQNk1xHYgqSJ+tM303rmHQBXK+LYyuvsIURlJh0jaIkhXSIIWiy+cot9fY+qGvZx75nnO/+N3WP3Gd7n02BP4cg1dTXDLHfovvgstT++V9wmnJ/BbitYPXyQY9/i4jk/GEJfBqI1kra/irVLeBcfx0SEbxOAUFAZb3U7qq2y+vYAnY6vXI6lPcvCPHmTnQ/fReuMK69/+T8r1hI0Tb9K/9D7JbXPEh67DpAW0W+QnTmFMjEgJRkMoQpyuUgQTR5yS48YF5bvEFqDAl2LwJZwU5Csdtt1ykOhSD9/LCLdNsvzUS7B3O2m2yXDhAkoLo7TP+tllOsOTTN5yA/F12xi79whBrcHgvWvIdBO3ZXFhhBQWkRyvuMsI+UHxDqSMDzymv4q4mKIPU0eP0F/cQl9aRd+8nUa1ydjhfQymt+GrmuHyNabu/jDNuz+KKQdk68t464gnZtC7JilGI0IcmAiGmyjXxUZjSJYeVKB25+VJoEBEcEGEq82SOmHt7YtoFWDKCbvvv4uxj99B0agRHztMEEww6DkERykusOstzOQ4VkWkF6+RX1mBpA7OI0WBQvDRNGiDjFo7lPeuKXkfPVgB28XFDWRtkWp5QDIdkeyfpd8f0j2ziN4zSXTTFJs/eIm8bancsB8xiuGFy+idTZyJSVcGVOemiHfOwmCIDK4hvg8ljdgOQXcBb2zVmOE63lYoomlUMUDcFtJdIYlGxHtnWH3+vxm1Nuj831mSksUPLL3nTiN3WtaeeY7ewhWClie+nGJ2T6AWl7H9ITqyBFOCdRM4XUIVA8h7+LyLD8eR9oWX33S+dNCFZcxohBXApYRpC+pNWosdVr/1FMHaCKWhfOsB/K076LxwmqzVpvmJY0x86k76T76KDAsY9CgmA6q3z2LqTYqigmRdUFV8sY53m6Arp42T0gdgD6IEG0ZIXiDeUEgF6Rbs/NljDE6do/cPP6J2z+1cOXOK0Wsn6J5bobZZYLSi/e55Zn/xLvzQka8aSnsSfFjGDUYo5XAmwCuHSIJYhdduSeHkTVSAFB4vGpEhyqUQ1xGfkbYuE95yPa5kKGLLtaWrtJ77MWVtiD99DMYa9F48z8bzrxP5ITqIKcIqsrKEeAUieEJk2EFlbXxQQXLeVBCesKaBHm79dAjJOEUyhXJ9CCMGgzKTxw/TvP8w7VffYn77LioTexEV4foFpXqdvQ9+kvqBWTZ++Ardi0uU6eOCBrY0Ccpgsi3ExHgzhuRd8KMTRqcrJ5WvvY6kt0pmUT5H5T1U1qao1FHFKroV0nzgI1x7/Sz5Qpv5ozfj911PcOMOkmqMxhKYgK1SgpssyM+fRZImuhYjEXiXgViU6+Oz1VcxlZOKwjmV9x+x5Rm8DsHmYEDUCMlTtCrwE9vRcx8i/WCFy6deoL2+ycSv3YXe1WDwzrusPPU8Hzz+FLVbb2TuzkMMVpYZrKzgBiO8b+Ark6Dkp7sR/sC7zBkX1A3e/YeM8iUfJju8AnElJAwxSZ1RKvROvUfv5f+lfeotvNLoX/gZJAd9foPVNy6z8L1/YdfRj1GZK2MGGeHcjWTXNP2ljKg0JIoKbDSJT9tXvMw841RsjC+ZWLm8613+AEXpR7oquLVVtq51GbYvMnrvEvmFFSo37KP2sY+gFvvsPHwTw80O/YUloqTKvvt/nW2f/TBGp+RrI3Rthsp4CdfvkHd62K0A3WhhYnufUEWhYum8/XLFlZOeVxFqmH8lu3Lu0Xyzz9BHDM+dJTCGaM9u6vv20F9a5vzfPEvJFzRuPkS20qayTTF230fpXl0mqlXJltfJ0xHJDdvR9QQZQNov8Kr4nbhW+jq13bjOuYqxcRkrJVS+gdfBY87UZyQ0X4wjhdqxCz1eobx/nlce+jP8lRUmjh5l9D+vsTbyrF6+xsz+Bo1fvRs91qC7cBUljsqBWXQQkfUsVmnC6eTPvZWvexeg+mdRkqO8ayO+DaLwqiCeb3xJ764/7G2fsFYDiTj923/J+r8/S3PyOkwnx8/PUt0zSWnUY/DOKqVaTNrtk11dQzcTXBDhPRhxBKH8Xt4tvozN0WaAGq0h1qPECsqBjxv4MKGwOWEz+Vo0v+vn4+3JT2zapbi6xfG/+guu/8KvMLZ/HrEFV79/AnNuCdcdsPTEf2GuDqjecQBTDpEcbEmfUXHyc6FSj+JyfF5CvKIwYzhtkI2Lb4AHbxQEEZ4AyTugCuiP0NnoU7bjv+Cmm8dbz/5YjFPobTXee+y7zBzYT9pqIXGZud+8F+qBK9L8BSXB4xLrfyuVI1wmuCSCaBKdd5BsFacE2bjw2jS26BNVQBtwQ3AF3iskz3siHjvwgStFx/uvnT1m0+xguH92VtayenTTdiSzndFGf8np4oy29iWphC96qwojFqlWKs4qQKFD0IxwOsI7X/5/BLkssNOLxIoAAAAASUVORK5CYII=',
            "title": "Automatic1111 webui",
            "repo_name": "stable-diffusion-webui",
            "github_url": "https://github.com/AUTOMATIC1111/stable-diffusion-webui",
            "git_clone_url":"https://github.com/AUTOMATIC1111/stable-diffusion-webui.git",
            "installed_version": "-",
            "available_version": "-",
            "installed": True,
            "visible":True,
            "status": 1,
            "type": "app",
            "install_requirements":False,
            "install_cuda":False,
            "entry_point": 
                {
                    "install":"webui-user.bat",
                    "launch":"launch.py",
                },  
            "buttons": [
                {
                    "button_text": "Install",
                    "key": "install",
                },
                # {
                #     "button_text": "Update",
                #     "key": "update",
                # },
                {
                    "button_text": "Delete venv",
                    "key": "delete_venv",
                },
                {
                    "button_text": "Create venv",
                    "key": "create_venv",
                },                        
                {
                    "button_text": "Uninstall",
                    "key": "uninstall",
                },                                               
            ],
            "launch_buttons": [
                {
                    "button_text": "Launch",
                    "key": "launch",
                },           
                {
                    "button_text": "Update",
                    "key": "update",
                },                                                 
            ],            
            "args": [
                [
                    {
                        "button_text": "--autolaunch",
                        "key": "autolaunch",
                    },  

                    {
                        "button_text": "--theme=dark",
                    },
                ],   
                [
                    {
                        "button_text": "--nowebui",
                        "key": "nowebui",
                    },    
                    {
                        "button_text": "--no-half",
                    }                      
                ],

                [
                    {
                        "button_text": "--force-enable-xformers",
                        "key": "force-enable-xformers",
                    },
                    {
                        "button_text": "--xformers",
                        "key": "xformers",
                    },
                ],                
                [
                    {
                        "button_text": "--lowvram",
                        "key": "lowvram",
                    },
                    {
                        "button_text": "--medvram",
                        "key": "medvram",
                    },
                    {
                        "button_text": "--lowram",
                        "key": "lowram",
                    },
                ],
                [
                    {
                        "button_text": "--share",
                        "key": "share",
                    },
                    {
                        "button_text": "--listen",
                        "key": "listen",
                    },

                    {
                        "button_text": "--api",
                        "key": "api",
                    },                    
                ],            
                [
                    {
                        "button_text": "--enable-insecure-extension-access",
                    },
                    
                ]
            ]
        },
        {
            "id": 2,
            "key": "app_",
            "image_path": b'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',
            "title": "Kohya's GUI",
            "repo_name": "kohya_ss",
            "github_url": "https://github.com/bmaltais/kohya_ss",
            "git_clone_url":"https://github.com/bmaltais/kohya_ss.git",
            "installed_version": "-",
            "available_version": "-",
            "installed": False,
            "visible":True,
            "status": 1,
            "type": "app",
            "install_requirements":False,
            "install_cuda":False,
            "download_models_path": "https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.safetensors",
            "checkpoints_path": "models\checkpoints",

            "entry_point": 
            {
                "install":"setup.bat",
                "launch":"gui.bat",
            },                      
            "buttons": [
                {
                    "button_text": "Install",
                    "key": "install",
                },
                {
                    "button_text": "Update",
                    "key": "update",
                },
                {
                    "button_text": "Delete venv",
                    "key": "delete_venv",
                },
                {
                    "button_text": "Create venv",
                    "key": "create_venv",
                },                        
                {
                    "button_text": "Uninstall",
                    "key": "uninstall",
                },                                              
            ],
            "launch_buttons": [
                {
                    "button_text": "Launch",
                    "key": "launch",
                },                                            
            ],            
            "args": [
                [
                    {
                        "button_text": "--inbrowser",
                        "key": "inbrowser",
                    },
                    {
                        "button_text": "--share",
                        "key": "share",
                    },                    
                ],               
            ]
        }, 
        {
            "id": 3,
            "key": "app_",
            "image_path": b'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',
            "title": "ComfyUI",
            "repo_name": "ComfyUI",
            "github_url": "https://github.com/comfyanonymous/ComfyUI",
            "git_clone_url":"https://github.com/comfyanonymous/ComfyUI.git",
            "installed_version": "-",
            "available_version": "-",
            "installed": False,
            "visible":True,
            "status": 1,
            "type": "app",
            "install_requirements":True,
            "install_cuda":True,
            "download_models_path": "https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.safetensors",
            "checkpoints_path": "models\checkpoints",

            "entry_point": 
            {
                "install":"main.py",
                "launch":"main.py",
            },                      
            "buttons": [
                {
                    "button_text": "Install",
                    "key": "install",
                },
                {
                    "button_text": "Update",
                    "key": "update",
                },
                {
                    "button_text": "Delete venv",
                    "key": "delete_venv",
                },
                {
                    "button_text": "Create venv",
                    "key": "create_venv",
                },                        
                {
                    "button_text": "Uninstall",
                    "key": "uninstall",
                },                                              
            ],
            "launch_buttons": [
                {
                    "button_text": "Launch",
                    "key": "launch",
                },                                            
            ],            
            "args": [
                [
                    {
                        "button_text": "--normalvram",
                        "key": "normalvram",
                    },
                    {
                        "button_text": "--listen",
                        "key": "listen",
                    },
                    {
                        "button_text": "--listen",
                        "key": "listen",
                    },                    
                ],               
            ]
        },        
        {
            "id": 4,
            "key": "app_",
            "image_path": b'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',
            "title": "Controlnet - webui extension",
            "repo_name": "sd-webui-controlnet",
            "github_url": "https://github.com/Mikubill/sd-webui-controlnet",
            "git_clone_url":"https://github.com/Mikubill/sd-webui-controlnet.git",
            "installed_version": "-",
            "available_version": "-",
            "installed": False,
            "visible":True,
            "status": 1,
            "type": "webui_extension",
            "webui_path": "stable-diffusion-webui",
            "models_path": "https://huggingface.co/datasets/disty/seait_ControlNet-modules-safetensors",
            "buttons": [
                {
                    "button_text": "Install",
                    "key": "install_webui_extension",
                },
                # {
                #     "button_text": "Install & Download Models",
                #     "key": "install_and_dl_all",
                # },                      
                {
                    "button_text": "Download Models",
                    "key": "download_models",
                },
                {
                    "button_text": "Update",
                    "key": "update_webui_extension",
                },                          
                {
                    "button_text": "Uninstall",
                    "key": "uninstall_webui_extension",
                },                                              
            ],
            "launch_buttons": [                                               
            ],  
            "args": [                                               
            ],                          
        },  
        # {
        #     "id": 5,
        #     "key": "app_",
        #     "image_path": b'iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAIAAAC0Ujn1AAAFEUlEQVR4nJ2W248UVRDGq+p09/QMM7M7goAIAVxkg+At8ICXB9EYFUmURGNiMDESEhOIf4f4gDHGgKJP6qsxGJREAUkEXOMFBFxuQVEEhV2Ya2/39Dn1+dCz7izOwsbKvEyfrl+f7+tTVc2VZfcTEwCoUlewCDPTzQJQKHomesREgBcEfhCCOjcxcZrENm3fhA74QejlAozDmTmNO4meGDNWq69a89iTmzY1Gw0xRtUViqUvP3j/u892Fcplda4nVoyJ6vWH16575KUNrUZDxKhqoVj8Ysf2H/d8USiXPSICwQtyhf5+CIsYdTqjr+zlcoQupWAiAhHzxEUAJgyLff1ELMaoaqFc8v0AABF5mX4AzlpYCwGcOmuBSdaDiFmZmEDUZRKgNksEoIrUAiBmIgio4zAz0/jvvxYzZ0gQdxR0LU0kUleiME36P3UwAR0o42Y3ExHJuNzpwHmS09NDTycyJqYjMAvvxstGhImYSAGdXFP/H81EqlprNGyaOkUulyuEOWMMjy+D6MZO9kSDmdvWzpp5y7vb3hiLou+PHT9weGj49Llq9WrHbkW5ryRsgCnpPdHMRM5qX7H49KOPENFz69ZC9ZczZ747cuzk2XOpTZfesfje5cteevW1dprKFAdsaq8ZqppaK8wK+J63fHBw+eDgdVu4wVvN0EyELuMmNBpjhFkAEEFVASICwMzW2amxXbsGdGrTOg9nkU4VAMys6H1g/nW/c67VpjSpO0ynU/fmujTNSlYIYOb2WNT9rkEU5mdY65zt3VGJyDlnrQvD/KSrqnHUJGYCBERiTG1k1LbTTldiAqF/9q3VZqPWqE+1u2q9Xm02SzMrADKRIpIk7drIiPE8EAkBYkxj9GoctcQYAphY03T+wMBotXZ0+BQzpWmKrminKTP/8POxarN1+8CATS0TE8BikqgZ1WrGGAIEgBgT1WrN0avZ01ikHcfzltw5a/6CN7fvJKIgCLgrckEAord2vD9n0cK5iwfSJGYREIzv1a9ciWo1MQaAEJHxvKjRuDA87PlB1ihU1cuFz27e8vlX+x5//sU9+w9cuny5GUXNKLr49+Xde/evWf/C14eH1m/eYnw/m9dQeL7/24kTcaslxlDn8AFi+JdDB1c+9RQLd1yLWoOrV7+ydevu93au3bCxUioWwhwRorH4WrM1946Bja9vHVi5KonGWISIWCRN4pOHDnqeNzHAVDUsFH49cuT88eML77k7abbEGBZJomjZAw8tXbnqwqlTl38/X79WJaZyf2XOwkXzB5eK58dRJMJEpM6FpdLpoaHfT5zI5fOZjk7JMIuq2//xhy+veIONAZRZWCRpNVlk4YoVi++7Lzs/ANTadhyj3c5qCKrG82wSf/3xR51hBtBEyaiGhcK5n47u3rE9LBaM8dQ5AJnYJIqieq1Vrbaq1ahWS6IocwCAOmd838+Hn739zh8nh3P5wr+fShPtSVULxRlDn35ik+SJjRuLlUoSj9l2mm2Bx1sRiADAORL2/CDIh/WRkT3bth3dtzdfmqE6UWJcuev+7lpgkbFGY+aCBavXPbPswQf65swWzxvnZdYRMxOxdWn177+Gvzn47a5d1UuX8qXidWPoejQRsRGbtNM4Kc+aNW/Jkv5582feNrdYqRjPJyLn2s1qbfTipWt//nHxzNnG6Igf5r0ggF7fEnqgM/ksYtM0jRPnHDGJCIsIyAFQB5Axxgtzvu9Dtees+QeTftpZqowBbwAAAABJRU5ErkJggg==',
        #     "title": "Controlnet -sd21_laion_face fork- webui extension",
        #     "repo_name": "sd-webui-controlnet",
        #     "github_url": "https://github.com/Mikubill/sd-webui-controlnet",
        #     "git_clone_url":"https://github.com/Mikubill/sd-webui-controlnet.git",
        #     "installed_version": "-",
        #     "available_version": "-",
        #     "installed": False,
        #     "visible":True,
        #     "status": 1,
        #     "type": "webui_extension",
        #     "webui_path": "stable-diffusion-webui",
        #     "models_path": "https://huggingface.co/datasets/disty/seait_ControlNet-modules-safetensors",
        #     "buttons": [
        #         {
        #             "button_text": "Install",
        #             "key": "install_webui_extension",
        #         },
        #         # {
        #         #     "button_text": "Install & Download Models",
        #         #     "key": "install_and_dl_all",
        #         # },                      
        #         {
        #             "button_text": "Download Models",
        #             "key": "download_models",
        #         },
        #         {
        #             "button_text": "Update",
        #             "key": "update_webui_extension",
        #         },                          
        #         {
        #             "button_text": "Uninstall",
        #             "key": "uninstall_webui_extension",
        #         },                                              
        #     ]
        # }, 
        {
            "id": 5,
            "key": "app_",
            "image_path": b'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',
            "title": "Dreambooth - webui extension",
            "repo_name": "sd_dreambooth_extension",
            "github_url": "https://github.com/d8ahazard/sd_dreambooth_extension",
            "git_clone_url":"https://github.com/d8ahazard/sd_dreambooth_extension.git",
            "installed_version": "-",
            "available_version": "-",
            "installed": False,
            "visible":True,
            "status": 1,
            "type": "webui_extension",
            "webui_path": "stable-diffusion-webui",
            "buttons": [
                {
                    "button_text": "Install",
                    "key": "install_webui_extension",
                },
                {
                    "button_text": "Update",
                    "key": "update_webui_extension",
                },
                {
                    "button_text": "Uninstall",
                    "key": "uninstall_webui_extension",
                },                                            
            ],
            "launch_buttons": [                                               
            ],  
            "args": [                                               
            ],               
        },       
        # {
        #     "id": 6,
        #     "key": "app_",
        #     "image_path": b'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',
        #     "title": "civitai",
        #     "repo_name": "civitai",
        #     "github_url": "https://github.com/civitai/sd_civitai_extension",
        #     "git_clone_url":"https://github.com/civitai/sd_civitai_extension.git",
        #     "installed_version": "-",
        #     "available_version": "-",
        #     "installed": False,
        #     "visible":True,
        #     "status": 1,
        #     "type": "webui_extension",
        #     "webui_path": "stable-diffusion-webui",
        #     "buttons": [
        #         {
        #             "button_text": "Install",
        #             "key": "install_webui_extension",
        #         },
        #         {
        #             "button_text": "Update",
        #             "key": "update_webui_extension",
        #         },
        #         {
        #             "button_text": "Uninstall",
        #             "key": "uninstall_webui_extension",
        #         },                                            
        #     ]
        # },        
        # 
        #                              
    ]
    