# contract-generator-pyside2
Another contract generator built on PySide2

Build:

`PYTHONOPTIMIZE=1 pyinstaller --clean --noconfirm contract_generator_app.spec`

Available Fields
  - Contract Templates
    - start_date
    - end_date
    - party_a_name
    - party_a_representative
    - party_a_registered_address
    - party_a_contact_address
    - party_b_name
    - party_b_representative
    - party_b_registered_address
    - party_b_contact_address
    - signature_date
    - payment_method
  - Payment Method Templates
    - currency
    - cross_border_payment
    - bank_account
    - account_name
    - name_of_the_bank
    - bank_code
    - name_of_the_branch
    - branch_code
    - country_of_the_bank_receiving_the_payment
    - swift_code
    - other_code
    - other_code_text